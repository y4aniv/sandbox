def create_table(n):
    """
    :entree: n: int
    :sortie: None
    """
    with open(f'table_de_{n}.txt', 'w') as f:
        i=0
        while i<11:
            f.write(f'{n}*{i} = {i*n}\n')
            i+=1

create_table(5)