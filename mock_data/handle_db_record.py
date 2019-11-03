import mock_data.utils.db_connector as db
import traceback


def find_xxx_id_by_a_num(a_num):
    sql = "abcde"
    list_val = [a_num, ]
    cursor.execute(sql, tuple(list_val))

    xxx_id = cursor.fetchall()
    return xxx_id[0][0]


def clear_table_yyy(certain_list):
    count_row = 0
    sql = "DELETE FROM yyy WHERE a_num=%s"
    for a in certain_list:
        list_val = [a, ]
        cursor.execute(sql, tuple(list_val))
        count_row += cursor.rowcount
    conn.commit()
    print(count_row, "行记录从yyy表删除。")


if __name__ == "__main__":
    try:
        conn = db.connect_to_db("aaa")
        cursor = conn.cursor()
        clear_table_yyy([1,2,3])

    except Exception as e:
        traceback.print_exc()
    finally:
        conn.close()
