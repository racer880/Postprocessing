function Diagram_Template(save_path, excel_path, a, b, c, d, e, f, g)

 % GUI erstellen
    fig = uifigure('Name', 'Customized Diagram', 'Position', [200, 200, 400, 600]);

    % Titel der GUI
    uicontrol('Parent', fig, 'Style', 'text', 'String', 'Customized Diagram', 'Position', [50, 570, 300, 20], 'FontSize', 12, 'FontWeight', 'bold');
    
     % Button "Durchsuchen" für Excel-Datei
    uicontrol('Parent', fig, 'Style', 'pushbutton', 'String', 'Durchsuchen', 'Position', [50, 520, 80, 20], 'Callback', @browseExcelFile);

     % Textfeld für den Dateinamen der Excel-Datei
    filename_text = uicontrol('Parent', fig, 'Style', 'text', 'String', '', 'Position', [140, 520, 220, 20]);

     % Excel-Datei einlesen (leer initialisieren)
    data = table();
    column_names = {};

    % Diagrammtitel
    uilabel(fig, 'Position', [20 480 200 22], 'Text', 'Diagrammtitel:');
    a = uitextarea(fig, 'Position', [220 480 160 22]);
    
    % Min_Wert_x_Achse
    uilabel(fig, 'Position', [20 440 200 22], 'Text', 'Min_Wert_x_Achse:');
    b = uitextarea(fig, 'Position', [220 440 160 22]);

    % Max_Wert_x_Achse
    uilabel(fig, 'Position', [20 400 200 22], 'Text', 'Max_Wert_x_Achse:');
    c = uitextarea(fig, 'Position', [220 400 160 22]);

    % Anzahl_Werte_pro_cm_x_Achse
    uilabel(fig, 'Position', [20 360 200 22], 'Text', 'Anzahl_Werte_pro_cm_x_Achse:');
    d = uitextarea(fig, 'Position', [220 360 160 22]);

    % Min_Wert_y_Achse
    uilabel(fig, 'Position', [20 320 200 22], 'Text', 'Min_Wert_y_Achse:');
    e = uitextarea(fig, 'Position', [220 320 160 22]);

    % Max_Wert_y_Achse
    uilabel(fig, 'Position', [20 280 200 22], 'Text', 'Max_Wert_y_Achse:');
    f = uitextarea(fig, 'Position', [220 280 160 22]);

    % Anzahl_Werte_pro_cm_y_Achse
    uilabel(fig, 'Position', [20 240 200 22], 'Text', 'Anzahl_Werte_pro_cm_y_Achse:');
    g = uitextarea(fig, 'Position', [220 240 160 22]);

    % Erstelle den Plot-Button
    btnPlot = uibutton(fig, 'push', 'Position', [160 50 80 22], 'Text', 'Plot');
    btnPlot.ButtonPushedFcn = @plotButtonPushed; % Setze die Callback-Funktion für den Button
    
    % Callback-Funktion zum Durchsuchen der Excel-Datei
    function browseExcelFile(~, ~)
        [filename, path] = uigetfile('*.xlsx;*.xls', 'Excel-Datei auswählen');
        if filename ~= 0
            % Excel-Datei einlesen
            excel_file = fullfile(path, filename);
            data = readtable(excel_file);
            column_names = data.Properties.VariableNames;
           
            
            % Dateiname anzeigen
            set(filename_text, 'String', filename);
        end
    end

    function plotButtonPushed(src, event)
        % Allgemeine Parameter
        % Plot_title = 'Template Diagrammerstellung';
        Plot_title = a;
        
        % Parameter auf x-Achse
         % Min_Wert_x_Achse = -20;
         % Max_Wert_x_Achse = 20;
         % Anzahl_Werte_pro_cm_x_Achse = 5;
         Min_Wert_x_Achse = b;
         Max_Wert_x_Achse = c;
         Anzahl_Werte_pro_cm_x_Achse = d;
       
        % Parameter auf y-Achse
         % Min_Wert_y_Achse = -1;
         % Max_Wert_y_Achse = 1;
         % Anzahl_Werte_pro_cm_y_Achse = 0.5;
         Min_Wert_y_Achse = e;
         Max_Wert_y_Achse = f;
         Anzahl_Werte_pro_cm_y_Achse = g;
    
        % Parameter - Platzhalter am Rand des Dokuments
        buffer = 5;
    
        % Berechnung 
        groesse_x_Achse = (Max_Wert_x_Achse - Min_Wert_x_Achse)/Anzahl_Werte_pro_cm_x_Achse;
        groesse_y_Achse = (Max_Wert_y_Achse - Min_Wert_y_Achse)/Anzahl_Werte_pro_cm_y_Achse;
    
        x_Achse_Beschriftung = ['x: ',num2str(groesse_x_Achse), '(cm)'];
        y_Achse_Beschriftung = ['y: ',num2str(groesse_y_Achse), '(cm)'];
    
    
        x1 = linspace(Min_Wert_x_Achse, Max_Wert_x_Achse, 100);
        % TO-DO: Implement Excel-path
        y1 = sin(x1);
    
      
        
        % Create the figure and subplots
        fig = figure(1);
        subplot(3, 1, 1);
        plot(x1, y1);
        grid on;
        xlabel(x_Achse_Beschriftung);
        ylabel(y_Achse_Beschriftung);
        axis tight;
        set(gca, 'Units', 'centimeters', 'Position', [buffer/2, buffer/2, groesse_x_Achse, groesse_y_Achse]); %Grössere Plot
        set(gca, 'XTick', Min_Wert_x_Achse:Anzahl_Werte_pro_cm_x_Achse:Max_Wert_x_Achse);
        set(gca, 'YTick', Min_Wert_y_Achse:Anzahl_Werte_pro_cm_y_Achse:Max_Wert_y_Achse);
        title(Plot_title);
    
        
        % Set the size of the figure in centimeters
        set(fig, 'Units', 'centimeters', 'Position', [0, 0, groesse_x_Achse + buffer, groesse_y_Achse + buffer]);
        set(fig,'Visible', 'on');
        
        % Saving parameter
        path = save_path;
        c = clock;
        c(1,6) = uint8(c(1,6));
        savetitle = [num2str(Plot_title), '_' , num2str(c(1,1)) , '_', num2str(c(1,2)) , '_', num2str(c(1,3)) , '_', num2str(c(1,4)), '_', num2str(c(1,5)), '_',num2str(c(1,6))];
        savetitle = savetitle(~isspace(savetitle));
        saveas(gcf,fullfile(path, savetitle));
    
        writeObj = VideoWriter('Diagram_Template', 'MPEG-4');
        open(writeObj);
        % Create a live point that floats on top of the sinus function
        hold on;
        h = plot(x1(1), y1(1), 'ro', 'MarkerFaceColor', 'r');
    
            % Loop through the x-axis values and update the position of the live point
        for i = 1:length(x1)
            set(h, 'XData', x1(i), 'YData', y1(i));
            % pause(0.01);
            F = getframe(fig);
            writeVideo(writeObj, F);
        end
        close(writeObj);
        end
        
end