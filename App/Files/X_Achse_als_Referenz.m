function X_Achse_als_Referenz(excel_file)
    % GUI erstellen
    fig = figure('Name', 'X-Achse als Referenz', 'Position', [800, 100, 400, 800]);
    
    % Titel der GUI
    uicontrol('Parent', fig, 'Style', 'text', 'String', '2D-Diagramm - X-Achse als Referenz', 'Position', [50, 750, 300, 20], 'FontSize', 12, 'FontWeight', 'bold');
    
    % Excel-Datei einlesen
    data = readtable(excel_file);
    column_names = data.Properties.VariableNames;
    
    % Dropdown-Menü für die Spaltenauswahl
    dropdowns = {};
    
    % X-Achse Dropdown-Menü
    uicontrol('Parent', fig, 'Style', 'text', 'String', 'X-Achse:', 'Position', [50, 680, 70, 20]);
    dropdowns{1} = uicontrol('Parent', fig, 'Style', 'popupmenu', 'String', column_names, 'Position', [130, 680, 220, 30]);
    
    % Anzahl der Y-Achsen Dropdown-Menü
    uicontrol('Parent', fig, 'Style', 'text', 'String', 'Anzahl der Y-Achsen:', 'Position', [50, 630, 120, 20]);
    y_axis_num_dropdown = uicontrol('Parent', fig, 'Style', 'popupmenu', 'String', cellstr(num2str((1:10)')), 'Position', [180, 630, 60, 30], 'Value', 10, 'Callback', @updateYAxisDropdowns);
    
    % Y-Achsen Dropdown-Menüs
    y_dropdowns = {};
    for i = 1:10
        uicontrol('Parent', fig, 'Style', 'text', 'String', ['Y' num2str(i) '-Achse:'], 'Position', [50, 580 - (i-1)*30, 70, 20]);
        y_dropdowns{i} = uicontrol('Parent', fig, 'Style', 'popupmenu', 'String', column_names, 'Position', [130, 570 - (i-1)*30, 220, 30]);
    end
    
    % Eingabefeld für Diagrammtitel
    uicontrol('Parent', fig, 'Style', 'text', 'String', 'Diagrammtitel:', 'Position', [50, 250, 80, 20]);
    title_edit = uicontrol('Parent', fig, 'Style', 'edit', 'Position', [130, 250, 220, 30]);
    
    % Button zum Erstellen des Plots
    plot_button = uicontrol('Parent', fig, 'Style', 'pushbutton', 'String', 'Plot erstellen', 'Position', [150, 50, 100, 30], 'Callback', @createPlot);

    % Button zum Schliessen
   closeButton = uicontrol(fig, 'Style', 'pushbutton', 'Position', [150,10, 100, 30], 'String', 'Close', 'Callback', @(src,evt) closeProgram(src,evt));
    
    % Callback-Funktion zum Aktualisieren der Y-Achsen Dropdown-Menüs
    function updateYAxisDropdowns(~, ~)
        % Anzahl der ausgewählten Y-Achsen erhalten
        y_axis_num = str2double(y_axis_num_dropdown.String{y_axis_num_dropdown.Value});
        
        % Dropdown-Menüs für die Y-Achsen basierend auf der Anzahl aktualisieren
        for i = 1:10
            if i <= y_axis_num
                set(y_dropdowns{i}, 'Visible', 'on');
            else
                set(y_dropdowns{i}, 'Visible', 'off');
            end
        end
        
        % GUI aktualisieren
        drawnow;
    end
    
    % Callback-Funktion zum Erstellen des Plots
    function createPlot(~, ~)
        % Ausgewählte Spalten für X- und Y-Achsen erhalten
        selected_x_column = dropdowns{1}.Value;
        selected_y_columns = [];
        for i = 1:numel(y_dropdowns)
            if strcmp(y_dropdowns{i}.Visible, 'on')
                selected_y_columns(end+1) = y_dropdowns{i}.Value;
            end
        end
        
        % Daten aus den ausgewählten Spalten lesen
        x_data = data.(column_names{selected_x_column});
        y_data = data{:, selected_y_columns};
        
        % Diagrammtitel erhalten
        diagram_title = get(title_edit, 'String');
        
        % Plot erstellen und anzeigen
        figure;
        plot(x_data, y_data);
        xlabel(column_names{selected_x_column});
        ylabel('Wert');
        title(diagram_title);
        legend(column_names(selected_y_columns), 'Location', 'best');
        grid on;
    end
% Function to close the program
    function closeProgram(~, ~)
        delete(fig);
    end
end


