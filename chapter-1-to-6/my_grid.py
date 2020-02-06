#my_grid.py (unfinished)
#last edited: 12/31/2019
#by: tran_dat_tin

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def gach_nho():
    print('-', end=' ') 

def in_bon_lan_gach_nho():
    do_four(gach_nho)
    print('+', end=' ')    

def in_hang_so_mot():
    print('+', end=' ')
    do_twice(in_bon_lan_gach_nho)

def khoang_trang():
    print(' ', end=' ')

def in_bon_lan_khoang_trang():    
    do_four(khoang_trang)
    print('|', end=' ')

def in_hang_so_hai():
    print('|', end=' ')
    do_twice(in_bon_lan_khoang_trang)
    print()

def in_4_lan_hang_so_hai():
	do_four(in_hang_so_hai)

def draw_full_grid():
    in_hang_so_mot()
    print()
    in_4_lan_hang_so_hai()
    

draw_full_grid()