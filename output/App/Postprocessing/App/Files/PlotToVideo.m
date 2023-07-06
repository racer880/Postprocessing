function PlotToVideo
    % Erstelle die GUI-Figur
    fig = uifigure('Name', 'Plot to Video - Skript');
    fig.Position = [100 100 600 350]; % Setze die Position der Figur
    
    % Erstelle den Titel
    titleText = uilabel(fig, 'Position', [0 310 600 30]);
    titleText.Text = 'Plot to Video - Skript';
    titleText.FontSize = 24;
    titleText.FontWeight = 'bold';
    titleText.HorizontalAlignment = 'center';
    
    % Erstelle den Durchsuchen-Button
    btnBrowse = uibutton(fig, 'push', 'Position', [20 250 100 22], 'Text', 'Durchsuchen');
    btnBrowse.ButtonPushedFcn = @browseButtonPushed; % Setze die Callback-Funktion für den Button
    
    % Erstelle das Label für den ausgewählten Dateipfad
    lblPath = uilabel(fig, 'Position', [220 250 540 22], 'HorizontalAlignment', 'left');
    lblPath.Text = 'Keine Datei ausgewählt';
    
    % Erstelle das erste Dropdown-Menü
    dropdownColumn1 = uidropdown(fig, 'Position', [20 200 160 22]);
    
    % Erstelle das zweite Dropdown-Menü
    dropdownColumn2 = uidropdown(fig, 'Position', [220 200 160 22]);
    
    % Erstelle das Textfeld für die Geschwindigkeit
    txtSpeedLabel = uilabel(fig, 'Position', [20 150 200 22], 'Text', 'Geschwindigkeit (10ms-1000ms):');
    txtSpeed = uitextarea(fig, 'Position', [220 150 160 22]);
    txtSpeed.Value = '10'; % Setze den Standardwert auf 100 ms
    
    % Erstelle den "Speicherort"-Button
    btnOutputPath = uibutton(fig, 'push', 'Position', [20 100 100 22], 'Text', 'Speicherort');
    btnOutputPath.ButtonPushedFcn = @outputPathButtonPushed; % Setze die Callback-Funktion für den Button
    
    % Erstelle das Label für den ausgewählten Speicherort
    lblOutputPath = uilabel(fig, 'Position', [220 100 540 22], 'HorizontalAlignment', 'left');
    lblOutputPath.Text = 'Kein Speicherort ausgewählt';
    
    % Erstelle den Plot-Button
    btnPlot = uibutton(fig, 'push', 'Position', [160 50 80 22], 'Text', 'Plot');
    btnPlot.ButtonPushedFcn = @plotButtonPushed; % Setze die Callback-Funktion für den Button
    
    % Callback-Funktion für den Durchsuchen-Button
    function browseButtonPushed(src, event)
        % Öffne den Dateiauswahldialog
        [filename, filepath] = uigetfile('*.xlsx', 'Excel-Datei auswählen');
        if isequal(filename,0) || isequal(filepath,0)
            % Benutzer hat Abbrechen gedrückt
            return;
        end
        
        % Zeige den ausgewählten Dateipfad im Label an
        selectedPath = fullfile(filepath, filename);
        lblPath.Text = selectedPath;
        
        % Lese die Excel-Datei ein
        [~, ~, data] = xlsread(selectedPath);
        
        % Extrahiere die erste Zeile jeder Spalte
        firstRow = data(1,:);
        
        % Aktualisiere die Dropdown-Menüs mit der ersten Zeile jeder Spalte
        dropdownColumn1.Items = firstRow;
        dropdownColumn2.Items = firstRow;
    end

    % Callback-Funktion für den "Speicherort"-Button
    function outputPathButtonPushed(src, event)
        % Öffne den Verzeichnisauswahldialog
        outputpath = uigetdir('', 'Speicherort auswählen');
        if isequal(outputpath,0)
            % Benutzer hat Abbrechen gedrückt
            return;
        end
        
        % Zeige den ausgewählten Speicherort im Label an
        lblOutputPath.Text = outputpath;
    end

    % Callback-Funktion für den Plot-Button
    function plotButtonPushed(src, event)
        % Lese den ausgewählten Dateipfad
        selectedPath = lblPath.Text;
        
        % Überprüfe, ob eine Datei ausgewählt wurde
        if strcmp(selectedPath, 'Keine Datei ausgewählt')
            errordlg('Bitte wählen Sie eine Excel-Datei aus.', 'Fehler');
            return;
        end
        
        % Lese die ausgewählten Spalten aus den Dropdown-Menüs
        column1 = dropdownColumn1.Value;
        column2 = dropdownColumn2.Value;
        
        % Lese die Geschwindigkeit aus dem Textfeld
        speed = str2double(txtSpeed.Value);
        
        % Überprüfe, ob die Geschwindigkeit ein gültiger Wert ist
        if isnan(speed) || speed <= 0
            errordlg('Bitte geben Sie eine gültige Geschwindigkeit ein.', 'Fehler');
            return;
        end
        
        % Lese die Daten aus der Excel-Datei
        [~, ~, data] = xlsread(selectedPath);
        
        % Finde die ausgewählten Spaltenindizes
        columnIdx1 = find(strcmp(data(1,:), column1));
        columnIdx2 = find(strcmp(data(1,:), column2));
        
        % Extrahiere die Daten aus den ausgewählten Spalten (ab Zeile 2)
        x = cell2mat(data(2:end, columnIdx1));
        y = cell2mat(data(2:end, columnIdx2));
        
        % Erstelle den Plot
        figure;
        plot(x, y);
        xlabel(['$', column1, '$'], 'Interpreter', 'latex');
        ylabel(['$', column2, '$'], 'Interpreter', 'latex');
        title('Plot');
        
        % Erstelle den "Follow-line" Punkt
        hold on;
        point = plot(x(1), y(1), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
        hold off;
        
        % Erstelle die MP4-Datei
        outputpath = lblOutputPath.Text;
        videoFile = VideoWriter(fullfile(outputpath, sprintf('plot_video_%s_%dms.mp4', datestr(now, 'yyyymmdd_HHMM'), speed)), 'MPEG-4');
        videoFile.FrameRate = 1000/speed; % Setze die Framerate basierend auf der Geschwindigkeit
        
        % Öffne die Video-Datei zum Schreiben
        open(videoFile);

        
        % Füge jeden Frame des Plots zum Video hinzu
        for i = 1:length(x)
            % Aktualisiere den Punkt, um der aktuellen Position zu folgen
            point.XData = x(i);
            point.YData = y(i);
            
            % Nehme den aktuellen Frame auf und füge ihn zum Video hinzu
            frame = getframe(gcf);
            writeVideo(videoFile, frame);
            
            % Warte entsprechend der Geschwindigkeit, bevor der nächste Frame aufgenommen wird
            pause(speed/1000);
        end
        
        % Schließe die Video-Datei
        close(videoFile);
        
        % Aktualisiere den Titel mit der Geschwindigkeit und der aktuellen Uhrzeit
        titleStr = sprintf('Plot (%d ms) - %s', speed, datestr(now, 'HH:MM'));
        title(titleStr);
    end
end
