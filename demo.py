
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import wx
import wx.xrc
 
def showchart():
    name_list = ['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
    num_list = [52.4, 57.8, 59.1, 54.6]
    rects=plt.bar(range(len(num_list)), num_list, color='rgby')
    # X轴标题
    index=[0,1,2,3]
    index=[float(c)+0.4 for c in index]
    plt.ylim(ymax=80, ymin=0)
    plt.xticks(index, name_list)
    plt.ylabel("arrucay(%)") #X轴标签
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height)+'%', ha='center', va='bottom')
    plt.show()
 
 
class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(571, 459),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)
        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_button8 = wx.Button(self, wx.ID_ANY, u"确定",
                                   wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer15.Add(self.m_button8, 0, wx.ALL, 5)
        bSizer11.Add(bSizer15, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer11)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button8.Bind(wx.EVT_BUTTON, self.m_button8OnButtonClick)
 
    def __del__(self):
        pass
    def m_button8OnButtonClick(self, event):
        showchart()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame(None)
    window.Show()
    app.MainLoop()
