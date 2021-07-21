import tools
import pymysql


def write(key):
    tag="中石油招标网"
    connect = pymysql.Connect(
        host='125.70.231.243',
        port=40004,
        user='root',
        passwd='123456',
        db='scrwaler',
        charset='utf8'
    )
    
    cursor = connect.cursor()
    dic = f'./files/{key}/'
    data = tools.readFromFile(f'{dic}result.json', )
    for row in data:
        sql = "select COUNT(*) from total where total.title = '{title}' and total.detailDesc = '{detailDesc}'  ".format(
            title=row['projectname'], detailDesc=row['dateTime'].split(" ")[0])

        cursor.execute(sql)
        diff = cursor.fetchall()
        num=diff[0][0]
        if num == 0:
            cursor.execute("insert into total (title,detailDesc,newsText,webSite) values (%s,%s,%s,%s) ",[row['projectname'],row['dateTime'].split(" ")[0],row['bulletincontent'],tag])

    print(cursor.rowcount, "record(s) affected")
    connect.commit()
    cursor.close()
    connect.close()



if __name__ == '__main__':
    write('地质灾害')
