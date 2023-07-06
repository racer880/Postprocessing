function Diagram_Template_2(file_path)
    
    % Prompt user to select Excel file
    path = file_path;
    
    % Read Excel file using MATLAB's "xlsread" function
    [~,sheets] = xlsfinfo(fullfile(path));
    [selection,ok] = listdlg('PromptString','Select a sheet:','SelectionMode','single','ListString',sheets);
    if ~ok
        error('No sheet selected');
    end
    sheetName = sheets{selection};
    [~,~,data] = xlsread(fullfile(path),sheetName);
    
    % Prompt user to select column for plotting
    [selection,ok] = listdlg('PromptString','Select a column:','SelectionMode','single','ListString',data(1,:));
    if ~ok
        error('No column selected');
    end
    columnName = data{1,selection};
    columnData = cell2mat(data(2:end,selection));
    
    % Plot the selected column
    plot(columnData);
    title(columnName);

    % Wait
    pause(10.0);


end