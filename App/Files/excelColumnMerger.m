function excelColumnMerger
    % GUI erstellen
    fig = figure('Name', 'Excel Column Merger', 'Position', [100, 100, 800, 600]);

    % Dateipfad-Arrays initialisieren
    filepaths = cell(8, 10);

    % Auswahloptionen erstellen
    numColumns = inputdlg('Geben Sie die Anzahl der Spalten ein (zwischen 2 und 8):', 'Anzahl der Spalten', [1, 50], {'2'});
    numColumns = str2double(numColumns{1});
    if isnan(numColumns) || numColumns < 2 || numColumns > 8
        errordlg('UngÃ¼ltige Eingabe. Es muss eine Zahl zwischen 2 und 8 sein.', 'Fehler');
        return;
    end

    for i = 1:numColumns
        createSelectionUI(20, 550 - (i-1)*50, i);
    end
    
    % Neue Excel-Datei erstellen Knopf erstellen
    createSaveButton(20, 50, numColumns);
    
    % Callback-Funktion fÃ¼r den "Durchsuchen"-Knopf
    function browseFiles(hObject, ~, selection)
        % Dateien auswÃ¤hlen
        [filenames, filepath] = uigetfile('*.xlsx', 'Dateien auswÃ¤hlen', 'MultiSelect', 'on');
        
        % ÃœberprÃ¼fen, ob mindestens eine Datei ausgewÃ¤hlt wurde
        if ~isequal(filenames, 0)
            % ÃœberprÃ¼fen, ob nur eine Datei ausgewÃ¤hlt wurde
            if ischar(filenames)
                filepaths{selection, 1} = fullfile(filepath, filenames);
            else
                % Mehrere Dateien ausgewÃ¤hlt
                for i = 1:length(filenames)
                    filepaths{selection, i} = fullfile(filepath, filenames{i});
                end
            end
            % Dateipfade anzeigen
            updateText(hObject, selection);
        end
    end

    % Funktion zum Aktualisieren des Texts und Dropdown-MenÃ¼s neben dem Knopf
    function updateText(hObject, selection)
        % Textfeld und Dropdown-MenÃ¼ abrufen
        text = findobj('Tag', ['text', num2str(selection)]);
        dropdown = findobj('Tag', ['dropdown', num2str(selection)]);
        
        textString = '';
        for i = 1:numel(filepaths(selection, :))
            if ~isempty(filepaths{selection, i})
                textString = [textString, filepaths{selection, i}, newline];
                % Excel-Datei einlesen
                [~, ~, raw] = xlsread(filepaths{selection, i});
                % Erste Zeile des Spalten-Headers abrufen
                columnHeaders = raw(1, :);
                % Dropdown-MenÃ¼ mit den Spalten-Headern erstellen
                set(dropdown, 'String', columnHeaders, 'Value', 1);
            end
        end
        set(text, 'String', textString);
    end

    % Funktion zum Erstellen einer Auswahloption
    function createSelectionUI(x, y, selection)
        % Durchsuchen-Knopf erstellen
        button = uicontrol('Style', 'pushbutton', 'String', 'Durchsuchen', 'Position', [x, y, 100, 30], 'Callback', {@browseFiles, selection});
        % Textfeld erstellen
        text = uicontrol('Style', 'text', 'Position', [x+120, y, 440, 30], 'Tag', ['text', num2str(selection)]);
        % Dropdown-MenÃ¼ erstellen
        dropdown = uicontrol('Style', 'popupmenu', 'Position', [x+570, y, 200, 30], 'Tag', ['dropdown', num2str(selection)]);
        
        % Callback-Funktion fÃ¼r das Dropdown-MenÃ¼
        set(dropdown, 'Callback', {@dropdownCallback, selection});
    end

    % Callback-Funktion fÃ¼r das Dropdown-MenÃ¼
    function dropdownCallback(hObject, ~, selection)
        % AusgewÃ¤hlter Spaltenindex abrufen
        selectedColumnIndex = get(hObject, 'Value');
        
        % AusgewÃ¤hlte Spalte anzeigen
        disp(['AusgewÃ¤hlte Spalte fÃ¼r Option ', num2str(selection), ': ', num2str(selectedColumnIndex)]);
    end

    % Funktion zum Erstellen des "Neue Excel-Datei erstellen"-Knopfs
    function createSaveButton(x, y, numColumns)
        % Knopf erstellen
        button = uicontrol('Style', 'pushbutton', 'String', 'Neue Excel-Datei erstellen', 'Position', [x, y, 200, 30], 'Callback', @saveButtonCallback);
        
        % Speichertort-Textfeld erstellen
        uicontrol('Style', 'text', 'Position', [x+220, y, 100, 30], 'String', 'Speichertort:');
        % Speichertort-Eingabefeld erstellen
        savePathInput = uicontrol('Style', 'edit', 'Position', [x+330, y, 200, 30]);
        
        % Dateiname-Textfeld erstellen
        uicontrol('Style', 'text', 'Position', [x+540, y, 100, 30], 'String', 'Dateiname:');
        % Dateiname-Eingabefeld erstellen
        saveFilenameInput = uicontrol('Style', 'edit', 'Position', [x+650, y, 120, 30]);
        
        % Callback-Funktion fÃ¼r den "Neue Excel-Datei erstellen"-Knopf
        function saveButtonCallback(~, ~)
            % Speicherort und Dateiname abrufen
            savePath = get(savePathInput, 'String');
            saveFilename = get(saveFilenameInput, 'String');
            
            % ÃœberprÃ¼fen, ob Speicherort und Dateiname angegeben wurden
            if isempty(savePath) || isempty(saveFilename)
                errordlg('Speicherort und Dateiname mÃ¼ssen angegeben werden.', 'Fehler');
                return;
            end
            
            % AusgewÃ¤hlte Spalten abrufen
            selectedColumns = cell(numColumns, 1);
            for i = 1:numColumns
                dropdown = findobj('Tag', ['dropdown', num2str(i)]);
                selectedColumns{i} = get(dropdown, 'Value');
            end
            
            % Neue Excel-Datei erstellen
            mergedData = cell(1, numColumns);
            for i = 1:numColumns
                for j = 1:numel(filepaths(i, :))
                    if ~isempty(filepaths{i, j})
                        data = readcell(filepaths{i, j});
                        selectedColumn = data(:, selectedColumns{i});
                        if isempty(mergedData{i})
                            mergedData{i} = selectedColumn;
                        else
                            mergedData{i} = [mergedData{i}; selectedColumn];
                        end
                    end
                end
            end
            
            % Neue Datei speichern
            saveFile = fullfile(savePath, [saveFilename, '.xlsx']);
            numData = max(cellfun(@numel, mergedData));
            dataToWrite = cell(numData, numColumns);
            for i = 1:numColumns
                dataToWrite(1:numel(mergedData{i}), i) = mergedData{i};
            end
            writecell(dataToWrite, saveFile);
            
            % Erfolgsnachricht anzeigen
            msgbox(['Die neue Excel-Datei wurde erfolgreich erstellt und unter dem Pfad ', saveFile, ' gespeichert.'], 'Erfolgreich');
        end
    end

end
