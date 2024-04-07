from multiprocessing import Process
from Tools.Printar import printar


def teste():
    if __name__ == '__main__':
    # printar.prin().printar_oi('2')

    # for i in range 3:
        Process(target=printar.printar_oi, args=('ythalo', )).start()
        Process(target=printar.printar_oi, args=('ryan', )).start()
        Process(target=printar.printar_oi, args=('carlos', )).start()
        Process(target=printar.printar_oi, args=('pereira', )).start()
    # Process(target=printar.printar_oi).start()

teste()