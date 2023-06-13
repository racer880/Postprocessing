function Diagram_Template(save_path, excel_path, a, b, c, d, e, f, g)

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
