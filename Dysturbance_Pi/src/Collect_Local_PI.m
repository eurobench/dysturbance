function [Stability_margin_matrix, Second_PI] = Collect_Local_PI(Tests_folders, Protocol)
%--------------------------------------------------------------------------
% Collect Local PI for the Dysturbance Tests
%
%
% Dysturbance - EuroBench Consortium
% Created By: Simone Monteleone
% mail: simone.monteleone@phd.unipi.it
%--------------------------------------------------------------------------

num_folder = size(Tests_folders,1);
num = 0;
for i = 1:num_folder
    local_folder = Tests_folders(i);
    OLD_FOLDER = cd(local_folder);
    Protocol_matrix = readtable("protocol_check.csv");
    Protocol_number = Protocol_matrix.Protocol_number;
    if Protocol_number == Protocol
        num = num + 1;
        cd("Local_PI");
        fileinfo = dir;
        all_files = fileinfo(~[fileinfo(:).isdir]);
        switch Protocol
            case 1
                for j = 1:numel(all_files)
                    clear Data Data_2;
                    if contains(all_files(j).name, "Stability_margin_")
                        Data = readtable(all_files(j).name);
                        Stability_margin_mat(num,:) = table2array(Data);
                    elseif contains(all_files(j).name, "Absorbed_energy_")
                        Data_2 = readtable(all_files(j).name);
                        Sec_PI(num,:) = table2array(Data_2);
                    elseif contains(all_files(j).name, "Fall_check_")
                        Check = readtable(all_files(j).name);
                        Check_Fall(num,:) = Check.checkForFall;
                    end
                end
                Stability_margin_matrix = [Stability_margin_mat,Check_Fall];
                Second_PI = [Sec_PI, Check_Fall];
            case 2
                for j = 1:numel(all_files)
                    if contains(all_files(j).name, "Stability_margin_")
                        Data = readtable(all_files(j).name);
                        Stability_margin_mat(num,:) = table2array(Data);
                    elseif contains(all_files(j).name, "Equivalent_impedance_")
                        Data_2 = readtable(all_files(j).name);
                        Sec_PI(num,:) = table2array(Data_2);
                    elseif contains(all_files(j).name, "Fall_check_")
                        Check = readtable(all_files(j).name);
                        Check_Fall(num,:) = Check.checkForFall;
                    end
                end
                Stability_margin_matrix = [Stability_margin_mat,Check_Fall];
                Second_PI = [Sec_PI, Check_Fall];
            case 3
                for j = 1:numel(all_files)
                    if contains(all_files(j).name, "Stability_margin_")
                        Data = readtable(all_files(j).name);
                        Stability_margin_mat(num,:) = table2array(Data);
                    elseif contains(all_files(j).name, "Equivalent_impedance_")
                        Data_2 = readtable(all_files(j).name);
                        Sec_PI(num,:) = table2array(Data_2);
                    elseif contains(all_files(j).name, "Fall_check_")
                        Check = readtable(all_files(j).name);
                        Check_Fall(num,:) = Check.checkForFall;
                    end
                end
                Stability_margin_matrix = [Stability_margin_mat,Check_Fall];
                Second_PI = [Sec_PI, Check_Fall];
            case 4
                for j = 1:numel(all_files)
                    if contains(all_files(j).name, "Stability_margin_")
                        Data = readtable(all_files(j).name);
                        Stability_margin_mat(num,:) = table2array(Data);
                    elseif contains(all_files(j).name, "Fall_check_")
                        Check = readtable(all_files(j).name);
                        Check_Fall(num,:) = Check.checkForFall;
                    end
                    
                end
                Sec_PI(num,:) = 0;
                Stability_margin_matrix = [Stability_margin_mat,Check_Fall];
                Second_PI = [Sec_PI, Check_Fall];
            case 5
                for j = 1:numel(all_files)
                    if contains(all_files(j).name, "Stability_margin_")
                        Data = readtable(all_files(j).name);
                        Stability_margin_mat(num,:) = table2array(Data);
                    elseif contains(all_files(j).name, "Fall_check_")
                        Check = readtable(all_files(j).name);
                        Check_Fall(num,:) = Check.checkForFall;
                    end
                    
                end
                Sec_PI(num,:) = 0;
                Stability_margin_matrix = [Stability_margin_mat,Check_Fall];
                Second_PI = [Sec_PI, Check_Fall];
        end
    end
    cd(OLD_FOLDER);
end
end