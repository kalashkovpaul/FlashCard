## Решение треугольника по координатам
## Автор: Калашков П.А. ИУ7-16Б

from math import sqrt, acos, degrees, radians, cos, fabs
## Ввод координат треугольника
ax, ay = map(int, input('Введите координаты первой точки: ').split())
bx, by = map(int, input('Введите координаты второй точки: ').split())
cx, cy = map(int, input('Введите координаты третьей точки: ').split())
## Вычисление длин для АВ, ВС и АС
ab = sqrt((bx - ax)**2 + (by - ay)**2)
bc = sqrt((cx - bx)**2 + (cy - by)**2)
ac = sqrt((cx - ax)**2 + (cy - ay)**2)
## Проверка на то, лежат ли три точки на одной прямой
if (abs(ab + ac - bc) <= 1e-5) or (abs(ab + bc - ac) <= 1e-5) or (abs(ac + bc - ab) <= 1e-5):
    print('Это прямая, а не треугольник :(')
else: 
    print('Длины сторон треугольника равны {:3.5g} {:3.5g} {:3.5g}'.format(ab, bc, ac))
    p = (ab + ac + bc) / 2
    ## нахождение углов из теоремы косинусов
    c = degrees(acos((bc*bc + ac*ac - ab*ab) / (2*bc*ac)))
    b = degrees(acos((ab*ab + bc*bc - ac*ac) / (2*ab*bc)))
    a = 180 - b - c
    print('Углы треугольника равны {:3.5g} {:3.5g} {:3.5g}'.format(a, b, c))
    ## нахождение наибольшего угла и рассчёт его биссектрисы
    if a <= c <= b or c <= a <= b: ## если угол В наибольший
        maxangle = b
        l = (2 * ab * bc * cos(radians(maxangle / 2))) / (ab + bc)
    if a <= b <= c or b <= a <= c: ## если угол C наибольший
        maxangle = c
        l = (2 * ac * bc * cos(radians(maxangle / 2))) / (ac + bc)
    if b <= c <= a or c <= b <= a: ## если угол А наибольший
        maxangle = a
        l = (2 * ac * ab * cos(radians(maxangle / 2))) / (ac + ab)
    print('Биссектриса наибольшего угла равна {:3.5g}'.format(l))
    ## нахождение наименьшего угла
    minangle = min(a, b, c)
    
    ## Определение, является ли треугольник равнобедренным
    if abs (ab - ac) <= 1e-5 or abs(ab - bc) <= 1e-5 or abs(ac - bc) <= 1e-5:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник не равнобедренный')
            ## Определение, какой треугольник (тупоугольный, прямоугольный, остроугольный)
    if abs(maxangle - 90) <= 1e-5:
        print('Треугольник прямоугольный')
    elif maxangle < 90:
        print('Треугольник остроугольный')
    else:
        print('Треугольник тупоугольный')
        
        
    ## Определение прямых. Если прямая параллельна оси y, апоминаем это истинностью логических переменных ..ort
    ## Прямая АВ
    if abs(ax - bx) <= 1e-5:
        abort = True ## если АВ параллельна оси y
    else:
        abort = False
        kab = (by - ay) / (bx - ax) ## коэффициент АВ
        bab = ay - kab * ax ## свободный член АВ
    ## Прямая ВС
    if abs(bx -cx) <= 1e-5:
        bcort = True ## если ВС параллельна оси y
    else:
        bcort = False
        kbc = (cy - by) / (cx - bx) ## коэффициент ВС
        bbc = by - kbc * bx ## свободный член ВС
    ## Прямая АС
    if abs(ax - cx) <= 1e-5:
        acort = True ## если АС параллельна оси y
    else:
        acort = False
        kac = (cy - ay) / (cx - ax) ## коэффициент АС
        bac = cy - kac * cx ## свободный член АС
    
    
    ## Ввод точки для определения, лежит ли она внутри треугольника
    x, y = map(int, input('Введите координаты точки: ').split())
    
    ## Определение, лежит ли заданная точка внутри треугольника
    
    ## Полуплоскость АВ
    ## переменная mab хранит 1, если заданная точка по одну сторону с точкой С
    ##                       0, если заданная точка лежит на АВ
    ##                      -1, если заданная точка лежит по разные стороны с точкой С
    
    if abort: ## если АВ параллельна оси y
        if x > 0 and cx > 0 or x < 0 and cx < 0 :
            mab = 1 ## если лежит по одну сторону
        elif x == cx == 0:
            mab = 0 ## если лежит на прямой
        else: 
            mab = -1 ## если лежит по другую сторону
    else: ## если не параллельна оси y
        delta = cy - kab * cx - bab ## определение стороны, по которую лежит точка С
        deltam = y - kab * x - bab ## определение стороны, по которую лежит заданная точка
        if delta > 0 and deltam > 0 or delta < 0 and deltam < 0:
            mab = 1 ## если лежит по одну сторону
        elif deltam == 0:
            mab = 0 ## если лежит на прямой
        else:
            mab = -1 ## если лежит по другую сторону
    ## Полуплоскость ВС
    ## переменная mbc хранит 1, если заданная точка по одну сторону с точкой A
    ##                       0, если заданная точка лежит на BC
    ##                      -1, если заданная точка лежит по разные стороны с точкой A
    if bcort: ## если АВ параллельна оси y
        if x > 0 and ax > 0 or x < 0 and ax < 0 :
            mbc = 1 ## если лежит по одну сторону
        elif x == ax == 0:
            mbc = 0 ## если лежит на прямой
        else: 
            mbc = -1 ## если лежит по другую сторону
    else: ## если не параллельна оси y
        delta = ay - kbc * ax - bbc ## определение стороны, по которую лежит точка А
        deltam = y - kbc * x - bbc ## определение стороны, по которую лежит заданная точка
        if delta > 0 and deltam > 0 or delta < 0 and deltam < 0:
            mbc = 1 ## если лежит по одну сторону
        elif deltam == 0:
            mbc = 0 ## если лежит на прямой
        else:
            mbc = -1 ## если лежит по другую сторону
            
    ## Полуплоскость АС
    ## переменная mac хранит 1, если заданная точка по одну сторону с точкой B
    ##                       0, если заданная точка лежит на AC
    ##                      -1, если заданная точка лежит по разные стороны с точкой B
    if acort:
        if x > 0 and bx > 0 or x < 0 and bx < 0 :
            mac = 1 ## если лежит по одну сторону
        elif x == bx and x == 0:
            mac = 0 ## если лежит на прямой
        else: 
            mac = -1## если лежит по другую сторону
    else: ## если не параллельна оси y
        delta = by - kac * bx - bac ## определение стороны, по которую лежит точка В
        deltam = y - kac * x - bac ## определение стороны, по которую лежит заданная точка
        if delta > 0 and deltam > 0 or delta < 0 and deltam < 0:
            mac = 1 ## если лежит по одну сторону 
        elif deltam == 0:
            mac = 0 ## если лежит на прямой
        else:
            mac = -1 ## если лежит по другую сторону
    ## непосредственно определение
    if mab == mbc and mbc == mac and mab == 1 or mab == 0 or mbc == 0 or mac == 0: 
        print('Принадлежит')
        ## Нахождение расстояния до прямых, содержащих стороны треугольника
        ## До прямой АВ
        if abort == True: ## если АВ параллельна оси y
            pab = fabs(x)
        else: ## если не параллельна - по формуле метода координат
            pab = fabs(kab * x - y + bab) / sqrt(kab*kab + 1)
        ## До прямой ВС
        if bcort == True: ## если ВС параллельна оси y
            pbc = fabs(x)
        else: ## если не параллельна - по формуле метода координат
            pbc = fabs(kbc * x - y + bbc) / sqrt(kbc*kbc + 1)
        ## До прямой АС
        if acort == True: ## если АС параллельна оси y
            pac = fabs(x)
        else: ## если не параллельна - по формуле метода координат
            pac = fabs(kac * x - y + bac) / sqrt(kac*kac + 1)
            
        ## находим ближайшую прямую
        ##if pab <= pbc <= pac or pab <= pac <= pbc: ## если АВ - ближайшая прямая
        ##    p = pab 
        ##elif pbc <= pab <= pac or pbc <= pac <= pab: ## если BC - ближайшая прямая
        ##    p = pbc
        ##else: ## если АС - ближайшая прямая
        ##    p = pac
        p = min(pac, pbc, pab)
        pmin = max(pac, pbc, pab)
        print('Расстояние от точки до наиболее удалённой стороны или её продолжения {:3.5g}'.format(pmin))
        print('Расстояние от точки до ближайшей стороны или её продолжения {:3.5g}'.format(p))
    else:
        print('Не принадлежит')
        
        
## Короткий способ определения, принадлежит или нет области треугольника
    ## Для этого точка должна лежать по одну сторону от прямых АВ, ВС и АС. Проверим это
##    k1 = (ax - x) * (by - ay) - (bx - ax) * (ay - y) ## Проверяем для прямой АВ
##    k2 = (bx - x) * (cy - by) - (cx - bx) * (by - y) ## Проверяем для прямой ВС
##    k3 = (cx - x) * (ay - cy) - (ax - cx) * (cy - y) ## Проверяем для прямой АС
    ## Если вычисленные значения одного знака, то лежит. Если равны нулю - то на сторонах 
##    if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0 or k1 == 0 or k2 == 0 or k3 == 0:
##        print('Принадлежит')
##    else:
##        print('Не принадлежит')




