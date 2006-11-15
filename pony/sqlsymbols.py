symbols = [ 'SELECT', # 'INSERT', 'UPDATE', 'DELETE',
            'FROM', 'LEFT_JOIN', 'WHERE', # 'GROUP_BY', 'HAVING',
            'UNION', 'INTERSECT', 'EXCEPT',
            'ORDER_BY', 'LIMIT', 'ASC', 'DESC',
            'DISTINCT', 'ALL', 'AGGREGATES',
            'COUNT', 'SUM', 'MIN', 'MAX', 'AVG',
            'TABLE', 'COLUMN', 'PARAM', 'VALUE', 'AND', 'OR', 'NOT',
            'EQ', 'NE', 'LT', 'LE', 'GT', 'GE', 'IS_NULL', 'IS_NOT_NULL',
            'LIKE', 'NOT_LIKE', 'BETWEEN', 'NOT_BETWEEN',
            'IN', 'NOT_IN', 'EXISTS', 'NOT_EXISTS',
            'ADD', 'SUB', 'MUL', 'DIV', 'CONCAT' ]

globals().update((s, s) for s in symbols)
