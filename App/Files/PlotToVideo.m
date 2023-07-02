% PlotToVideo.m

% Erstelle eine GUI zur Auswahl der Excel-Datei und der Spalten
fig = figure('Name', 'Excel-Daten auswählen', 'NumberTitle', 'off', 'Position', [500, 400, 400, 250]);

excel_btn = uicontrol('Style', 'pushbutton', 'String', 'Excel-Datei auswählen', 'Position', [20, 180, 120, 30], 'Callback', @selectExcel);
excel_path_txt = uicontrol('Style', 'text', 'String', '', 'Position', [150, 185, 220, 20]);

col1_dropdown = uicontrol('Style', 'popupmenu', 'Position', [20, 140, 180, 30]);
col2_dropdown = uicontrol('Style', 'popupmenu', 'Position', [200, 140, 180, 30]);

plot_btn = uicontrol('Style', 'pushbutton', 'String', 'Plot erstellen', 'Position', [150, 80, 100, 30], 'Callback', @createPlot);

% Callback-Funktion zur Auswahl der Excel-Datei
function selectExcel(~, ~)
    [file, path] = uigetfile('*.xlsx', 'Excel-Datei auswählen');
    if file ~= 0
        excel_path = fullfile(path, file);
        excel_path_txt.String = excel_path;
        
        % Lese die Spaltennamen und Daten aus der Excel-Datei
        [~, ~, raw] = xlsread(excel_path);
        column_names = raw(1, :);
        data = raw(2:end, :);
        
        % Aktualisiere die Dropdown-Menüs mit den Spaltennamen
        set(col1_dropdown, 'String', column_names);
        set(col2_dropdown, 'String', column_names);
        
        % Aktualisiere die Dropdown-Menüs mit den ersten Zeilen der Spaltenwerte
        set(col1_dropdown, 'Value', 1);
        set(col2_dropdown, 'Value', 1);
        selectColumn(col1_dropdown, data);
        selectColumn(col2_dropdown, data);
    end
end

% Callback-Funktion zur Auswahl der Spalte
function selectColumn(dropdown, data)
    selected_column = dropdown.Value;
    
    % Zeige die ersten Zeilen der ausgewählten Spalte im Dropdown-Menü an
    selected_data = data(2:end, selected_column);
    set(dropdown, 'String', [column_names(selected_column), selected_data']);
end

% Callback-Funktion zum Erstellen des Plots
function createPlot(~, ~)
    % Hole die ausgewählten Spalten
    col1 = col1_dropdown.Value;
    col2 = col2_dropdown.Value;
    
    % Lese die Daten aus der Excel-Datei
    [~, ~, raw] = xlsread(excel_path_txt.String);
    
    % Hole die ausgewählten Daten aus den Spalten
    data1 = cell2mat(raw(2:end, col1));
    data2 = cell2mat(raw(2:end, col2));
    
    % Führe hier den Plot-Code mit den ausgewählten Daten durch
end
