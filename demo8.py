#!/usr/bin/env python

import wx
import wx.dataview as dv


musicdata = {
1 : ("Bad English", "The Price Of Love", "Rock"),
2 : ("DNA featuring Suzanne Vega", "Tom's Diner", "Rock"),
3 : ("George Michael", "Praying For Time", "Rock"),
4 : ("Gloria Estefan", "Here We Are", "Rock"),
5 : ("Linda Ronstadt", "Don't Know Much", "Rock"),
}

class TestModel(dv.DataViewIndexListModel):
    def __init__(self, data):
        dv.DataViewIndexListModel.__init__(self, len(data))
        self.data = data

    def GetColumnType(self, col):
        return "string"

    def GetValueByRow(self, row, col):
        return self.data[row][col]

    def SetValueByRow(self, value, row, col):
        self.data[row][col] = value
        return True

    def GetColumnCount(self):
        return len(self.data[0])

    def GetCount(self):
        return len(self.data)

    def GetAttrByRow(self, row, col, attr):
        if col == 3:
            attr.SetColour('blue')
            attr.SetBold(True)
            return True
        return False

    def Compare(self, item1, item2, col, ascending):
        if not ascending: # swap sort order?
            item2, item1 = item1, item2
        row1 = self.GetRow(item1)
        row2 = self.GetRow(item2)
        if col == 0:
            return cmp(int(self.data[row1][col]), int(self.data[row2][col]))
        else:
            return cmp(self.data[row1][col], self.data[row2][col])


    def DeleteRows(self, rows):
        rows = list(rows)
        rows.sort(reverse=True)

        for row in rows:
            del self.data[row]
            self.RowDeleted(row)


    def AddRow(self, value):
        self.data.append(value)
        self.RowAppended()



class TestPanel(wx.Panel):
    def __init__(self, parent, model=None, data=None):
        wx.Panel.__init__(self, parent, -1)

        # Create a dataview control
        self.dvc = dv.DataViewCtrl(self,
                                   style=wx.BORDER_THEME
                                   | dv.DV_ROW_LINES # nice alternating bg colors
                                   #| dv.DV_HORIZ_RULES
                                   | dv.DV_VERT_RULES
                                   | dv.DV_MULTIPLE
                                   )

        # Create an instance of our simple model...
        if model is None:
            self.model = TestModel(data)
        else:
            self.model = model

        self.dvc.AssociateModel(self.model)

        self.dvc.AppendTextColumn("Artist",  1, width=170, mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Title",   2, width=260, mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Genre",   3, width=80,  mode=dv.DATAVIEW_CELL_EDITABLE)

        c0 = self.dvc.PrependTextColumn("Id", 0, width=40)

        c0.Alignment = wx.ALIGN_RIGHT
        c0.Renderer.Alignment = wx.ALIGN_RIGHT
        c0.MinWidth = 40

        for c in self.dvc.Columns:
            c.Sortable = True
            c.Reorderable = True

        c0.Reorderable = False

        # set the Sizer property (same as SetSizer)
        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.dvc, 1, wx.EXPAND)


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
        # wx.FileSelector("Choose a file to open")

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


app = wx.App()
a = MyFrame1(None)
musicdata = sorted(musicdata.items())
musicdata = [[str(k)] + list(v) for k,v in musicdata]
win = TestPanel(a, data=musicdata)
a.Show(True)
app.MainLoop()