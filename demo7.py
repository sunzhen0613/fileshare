#!/usr/bin/env python

import wx
from wx.lib.itemspicker import ItemsPicker, \
                               EVT_IP_SELECTION_CHANGED, \
                               IP_SORT_CHOICES, IP_SORT_SELECTED,\
                               IP_REMOVE_FROM_CHOICES

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        box = wx.StaticBox(self,-1,"ItemPicker styles")
        boxSizer = wx.StaticBoxSizer(box,wx.VERTICAL)
        self.sortChoices = wx.CheckBox(self,-1,'IP_SORT_CHOICES')
        boxSizer.Add(self.sortChoices)
        self.sortSelected = wx.CheckBox(self,-1,'IP_SORT_SELECTED')
        boxSizer.Add(self.sortSelected)
        self.removeFromChoices = wx.CheckBox(self,-1,'IP_REMOVE_FROM_CHOICES')
        boxSizer.Add(self.removeFromChoices)
        sizer.Add(boxSizer,0,wx.ALL,10)
        b = wx.Button(self,-1,"Go")
        b.Bind(wx.EVT_BUTTON,self.Go)
        sizer.Add(b,0,wx.ALL,10)
        self.SetSizer(sizer)

    def Go(self,e):
        style = 0
        if self.sortChoices.GetValue():
            style |= IP_SORT_CHOICES
        if self.sortSelected.GetValue():
            style |= IP_SORT_SELECTED
        if self.removeFromChoices.GetValue():
            style |= IP_REMOVE_FROM_CHOICES
        d = ItemsPickerDialog(self, style)
        d.ShowModal()


class ItemsPickerDialog(wx.Dialog):
    def __init__(self,parent, style):
        wx.Dialog.__init__(self,parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        b = wx.Button(self, -1, "Add Item")
        b.Bind(wx.EVT_BUTTON, self.OnAdd)
        sizer.Add(b, 0, wx.ALL, 5)
        self.ip = ItemsPicker(self,-1,
                          ['ThisIsItem3','ThisIsItem2','ThisIsItem1'],
                          'Stuff:', 'Selected stuff:',ipStyle = style)
        self.ip.Bind(EVT_IP_SELECTION_CHANGED, self.OnSelectionChange)
        self.ip._source.SetMinSize((-1,150))

        # Customize the buttons for this example.
        if 'wxMac' not in wx.PlatformInfo:
            # NOTE: wx.Button on OSX does not modify the button size when adding a
            # bitmap after the fact like this, and these bitmaps are a little too
            # large and look funny in OSX, so we won't do this customization there.
            self.ip.bAdd.SetLabel('Add')
            self.ip.bRemove.SetLabel('Remove')

        sizer.Add(self.ip, 0, wx.ALL, 10)
        self.SetSizer(sizer)
        self.itemCount = 3
        self.Fit()


    def OnAdd(self,e):
        items = self.ip.GetItems()
        self.itemCount += 1
        newItem = "item%d" % self.itemCount
        self.ip.SetItems(items + [newItem])


    def OnSelectionChange(self, e):
        pass


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(500, 300),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        # f = MyPanel1(self)
        # wx.FileSelector("Choose a file to open")

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


app = wx.App()
a = MyFrame1(None)
f = TestPanel(a)
a.Show(True)
app.MainLoop()