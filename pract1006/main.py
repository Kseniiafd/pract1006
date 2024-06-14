import sqlite3

import config
import fnctn

def main():
    while True:
        action = input("Ввод : ")
        if action == "parse":
            if config.logs:
                
                conn = sqlite3.connect(config.db_name)
                cursor = conn.cursor()
                fnctn.dlt_table(cursor)
                for log_line in config.logs.split('\n'):
                    log_data = fnctn.prs_log_line(log_line)
                    if log_data:
                        fnctn.paste_logs_to_db(cursor, log_data)
                
                
                conn.commit()
                conn.close()
                print("Отлично")
            else:
                print("Отсутствие логов")
        else:
            conn = sqlite3.connect(config.db_name)
            cursor = conn.cursor()
            filters = action.split()
            all_data = fnctn.rcv_logs_from_db(cursor, config.table_name)
            filtered_data = fnctn.fltr_data(all_data, filters)
            for row in filtered_data:
                print(row)
            conn.commit()
            conn.close()

    
    
if __name__ == "__main__":
    main()
