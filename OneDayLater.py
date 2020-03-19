#Core of the game by ibuki
#用于模拟一天的传染/死亡。需要从data获得数据。

def one_day_later():
    global pop,inf,inf_rate,touch,rec,rec_rate,preinf,dead,dead_rate,vac,vac_rate
    dead += dead_rate * inf
    rec_ = inf * rec_rate
    vac_ = rec_ * vac_rate
    vac += vac_
    rec += rec_ - vac
    inf_ = preinf * inf_rate
    preInf += inf * touch *(1 - (inf + vac) / (pop - dead))
    inf += inf_
    preinf -= inf_
    rest = pop - vac - inf - dead

