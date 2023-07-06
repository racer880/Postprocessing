function customizedDiagram
    % GUI erstellen
    fig = uifigure('Name', 'customizedDiagram', 'Position', [100 100 400 250]);
    
    % UI-Komponenten erstellen
    btnBrowse = uibutton(fig, 'Text', 'Durchsuchen', 'Position', [10 190 80 20], 'ButtonPushedFcn', @browseButtonCallback);
    txtPath = uitextarea(fig, 'Position', [100 190 290 20], 'Editable', 'off');
    
    % Dropdown-Menüs erstellen
    lblXAxis = uilabel(fig, 'Text', 'X-Achse:', 'Position', [10 150 50 20]);
    ddXAxis = uidropdown(fig, 'Position', [70 150 150 20]);
    
    lblYAxis = uilabel(fig, 'Text', 'Y-Achse:', 'Position', [10 110 50 20]);
    ddYAxis = uidropdown(fig, 'Position', [70 110 150 20]);
    
    % Eingabefelder für minimale Werte erstellen
    lblMinX = uilabel(fig, 'Text', 'Min X:', 'Position', [10 70 50 20]);
    txtMinX = uieditfield(fig, 'numeric', 'Position', [70 70 60 20]);
    
    lblMinY = uilabel(fig, 'Text', 'Min Y:', 'Position', [10 30 50 20]);
    txtMinY = uieditfield(fig, 'numeric', 'Position', [70 30 60 20]);
    
    % Schrittweiten-Eingabefelder erstellen
    lblXStep = uilabel(fig, 'Text', 'X-Schrittweite:', 'Position', [150 70 80 20]);
    txtXStep = uieditfield(fig, 'numeric', 'Position', [240 70 60 20]);
    
    lblYStep = uilabel(fig, 'Text', 'Y-Schrittweite:', 'Position', [150 30 80 20]);
    txtYStep = uieditfield(fig, 'numeric', 'Position', [240 30 60 20]);
    
    % Plot-Button erstellen
    btnPlot = uibutton(fig, 'Text', 'Plot', 'Position', [10 10 80 20], 'ButtonPushedFcn', @plotButtonCallback);
    
    % Button-Klick-Callback-Funktion für den Durchsuchen-Button
    function browseButtonCallback(~, ~)
        % Dialog zum Auswählen einer Excel-Datei anzeigen
        [filename, pathname] = uigetfile('*.xlsx', 'Excel-Tabelle auswählen');
    
        % Überprüfen, ob eine Datei ausgewählt wurde
        if isequal(filename, 0)
            return; % Benutzer hat den Dialog abgebrochen
        end
    
        % Vollständigen Pfad zur ausgewählten Datei erstellen
        filepath = fullfile(pathname, filename);
    
        % Pfad im Textfeld anzeigen
        txtPath.Value = filepath;
    
        % Excel-Daten laden und Dropdown-Menüs aktualisieren
        data = readtable(filepath);
        columnNames = data.Properties.VariableNames;
        ddXAxis.Items = columnNames;
        ddYAxis.Items = columnNames;
    end


    % Button-Klick-Callback-Funktion für den Plot-Button
    function plotButtonCallback(~, ~)
        % Überprüfen, ob eine Datei ausgewählt wurde
        if isempty(txtPath.Value)
            return; % Keine Datei ausgewählt
        end
        
        % X- und Y-Achsenwerte auswählen
        xAxis = ddXAxis.Value;
        yAxis = ddYAxis.Value;
        
        % Excel-Daten laden und ausgewählte Spalten extrahieren
        data = readtable(txtPath.Value);
        xData = data.(xAxis);
        yData = data.(yAxis);
        
        % Minimale Werte für X und Y abrufen
        minX = txtMinX.Value;
        minY = txtMinY.Value;
        
        % Schrittweiten für X und Y abrufen
        xStep = txtXStep.Value;
        yStep = txtYStep.Value;
        
        % X- und Y-Achsenwerte generieren
        newXData = minX:xStep:max(xData);
        newYData = minY:yStep:max(yData);
        
        % Diagramm erstellen
        figure;
        plot(xData, yData);
        xlabel(xAxis);
        ylabel(yAxis);
        title('Customized Diagram');
        
        % Neuen Plot mit angepassten Schrittweiten erstellen
        figure;
        plot(newXData, newYData);
        xlabel(xAxis);
        ylabel(yAxis);
        title('Customized Diagram with Adjusted Step Size');
    end
end
