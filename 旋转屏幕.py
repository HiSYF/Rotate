import win32api
import win32con
import time

x,y = win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
def change_display_direction(angle):
    device = win32api.EnumDisplayDevices(None,0);
    dm = win32api.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)

    if angle == 90:
        dm.DisplayOrientation = win32con.DMDO_90#待改变的值
        #以下的720或者1280 代表我的屏幕的长宽
        #在应用项目的时候,建议使用GetSystemMetrics 动态获取长宽
        #在每次改变方向的时候,都要判断是否需要交换屏幕的长宽
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != y: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
     
    elif angle == 180:
        dm.DisplayOrientation = win32con.DMDO_180
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != x: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

    elif angle == 270:
        dm.DisplayOrientation = win32con.DMDO_270
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != y: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

    elif angle == 0:
        dm.DisplayOrientation = win32con.DMDO_DEFAULT
        if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != x: 
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    win32api.ChangeDisplaySettingsEx(device.DeviceName,dm)

# change_display_direction(90)
# time.sleep(20)
# change_display_direction(0)

while True:
    a = input("123+++")
    change_display_direction(int(a))
    

