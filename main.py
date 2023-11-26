import pandas as pd
from sqlalchemy import select, ColumnClause
from sqlalchemy.dialects.postgresql import Any

from moduls.connection import Session_edu
from moduls.orders import Orders
from moduls.users import Users
from moduls.product import Product
from moduls.work import Work
from moduls.product_type import Product_type


# def query_rows(table, *columns: ColumnClause[Any]):
#     query = select(columns).select_from(table)
#     result = session.execute(query).mappings().all()
#     print(pd.DataFrame(result))


if __name__ == '__main__':
    with Session_edu.begin() as session:
        #users_query = select(Users.user_id, Users.user_age, Users.user_name, Users.fk_job_id).select_from(Users)
        #users_query_result = session.execute(users_query).mappings().all()
        users_query_result = session.query(Users).all()
        #print(pd.DataFrame(users_query_result))
        for r in users_query_result:
            print(r)

        #orders_query = select(Orders.code, Orders.date, Orders.fk_user_code, Orders.order_products).select_from(Orders)
        #orders_query_result = session.execute(orders_query).mappings().all()
        orders_query_result = session.query(Orders).all()
        for s in orders_query_result:
            print(s)

        product_query = select(Product.code, Product.product_name, Product.price, Product.fk_type_code).select_from(Product)
        product_query_result = session.execute(product_query).mappings().all()
        print(pd.DataFrame(product_query_result))
        work_query = select(Work.job_id, Work.job_name, Work.salary).select_from(Work)
        work_query_result = session.execute(work_query).mappings().all()
        print(pd.DataFrame(work_query_result))
        product_type_query = select(Product_type.code, Product_type.pname).select_from(Product_type)
        product_type_query_result = session.execute(product_type_query).mappings().all()
        print(pd.DataFrame(product_type_query_result))
        # order_product_query = select(Order_product.fk_order_code, Order_product.fk_product_code, Order_product.quantity).select_from(Order_product)
        # order_product_query_result = session.execute(order_product_query).mappings().all()
        # print(pd.DataFrame(order_product_query_result))

