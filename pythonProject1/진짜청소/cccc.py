# include <iostream>
# include <mysql.h>

using
namespace
std;

# define DB_HOST "127.0.0.1"
# define DB_USER "root"
# define DB_PASS "0623"
# define DB_NAME "star_bucks"

void
main()
{
    MYSQL
conn;
MYSQL * conn_result;
MYSQL_RES * result;
MYSQL_ROW
row;
int
query_state;
unsigned
int
timeout_sec = 1;

mysql_init( & conn);
mysql_options( & conn, MYSQL_OPT_CONNECT_TIMEOUT, (const char *) & timeout_sec);
conn_result = mysql_real_connect( & conn, DB_HOST, DB_USER, DB_PASS, DB_NAME, 3306, (const char *)
NULL, 0);

if (conn_result = NULL)
{
cout << "DB connection Failre" << endl;
return;
}

else
{
cout << "DB Connection Success" << endl;

mysql_query(conn_result, "set session character_set_connection=euckr;");
mysql_query(conn_result, "set session character_set_results=euckr;");
mysql_query(conn_result, "set session character_set_client=euckr;");

const
char * query = "SELECT * FROM join_data";
query_state = mysql_query(conn_result, query);

if (query_state)
    {
        cout << "Query Error : " << mysql_error( & conn) << endl;
    cout << "QUery_state : " << mysql_query(conn_result, query) << endl;
return;
}

result = mysql_store_result(conn_result);
int
column_cnt = mysql_num_fields(result);

while (row = mysql_fetch_row(result))
{
for (int i = 0; i < column_cnt; i++)
{
    cout << row[i] << "\t;";
}
cout << endl;
}

mysql_free_result(result);
mysql_close( & conn);
}

return;
}
