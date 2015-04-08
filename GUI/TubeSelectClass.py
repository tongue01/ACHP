# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Fri Jun 18 22:24:04 2010

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class TubeSelectClass(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TubeSelectClass.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_10 = wx.StaticText(self, -1, "Material")
        self.cmbMaterial = wx.ComboBox(self, -1, choices=["Copper - Type L", "Steel - Schedule 40", "PVC - Schedule 40"], style=wx.CB_DROPDOWN)
        self.label_12 = wx.StaticText(self, -1, "Nom. Dimension")
        self.cmbNomDim = wx.ComboBox(self, -1, choices=["1/4 \"", "3/8 \"", "1/2 \"", "5/8 \"", "3/4 \"", "1 \"", "1-1/4 \"", "1-1/2 \"", "2 \""], style=wx.CB_DROPDOWN)
        self.cmdUpdate = wx.Button(self, -1, "Update...")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.updateDims, self.cmdUpdate)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: TubeSelectClass.__set_properties
        self.SetTitle("Tube Selection")
        self.label_10.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cmbMaterial.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cmbMaterial.SetSelection(0)
        self.label_12.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cmbNomDim.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cmbNomDim.SetSelection(2)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: TubeSelectClass.__do_layout
        grid_sizer_3 = wx.GridSizer(3, 2, 0, 0)
        grid_sizer_3.Add(self.label_10, 0, 0, 0)
        grid_sizer_3.Add(self.cmbMaterial, 0, 0, 0)
        grid_sizer_3.Add(self.label_12, 0, 0, 0)
        grid_sizer_3.Add(self.cmbNomDim, 0, 0, 0)
        grid_sizer_3.Add((20, 20), 0, 0, 0)
        grid_sizer_3.Add(self.cmdUpdate, 0, 0, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        self.Layout()
        # end wxGlade
        
    def setTarget(self,ODTarget,IDTarget):
        self.ODTarget=ODTarget
        self.IDTarget=IDTarget

    def updateDims(self, event): # wxGlade: TubeSelectClass.<event_handler>
        
        OD=0.0
        ID=0.0
        isOK=True
        if self.cmbMaterial.GetValue()=="Copper - Type L":
            NomDim=self.cmbNomDim.GetValue()
            if NomDim=='1/4 \"':
                OD=0.375
                ID=OD-0.030*2
            elif NomDim=='3/8 \"':
                OD=0.500
                ID=OD-0.035*2
            elif NomDim=='1/2 \"':
                OD=0.625
                ID=OD-0.040*2
            elif NomDim=='5/8 \"':
                OD=0.750
                ID=OD-0.042*2
            elif NomDim=='3/4 \"':
                OD=0.875
                ID=OD-0.045*2
            elif NomDim=='1 \"':
                OD=1.125
                ID=OD-0.050*2
            elif NomDim=='1-1/4 \"':
                OD=1.375
                ID=OD-0.055*2
            elif NomDim=='1-1/2 \"':
                OD=1.625
                ID=OD-0.060*2
            elif NomDim=='2 \"':
                OD=2.125
                ID=OD-0.070*2
            else:
                print "Invalid selection"
                isOK=False
                
        if self.cmbMaterial.GetValue()=="PVC - Schedule 40":
            NomDim=self.cmbNomDim.GetValue()
            if NomDim=='1/2 \"':
                OD=0.840
                ID=OD-0.109*2
            elif NomDim=='3/4 \"':
                OD=1.050
                ID=OD-0.113*2
            elif NomDim=='1 \"':
                OD=1.315
                ID=OD-0.133*2
            elif NomDim=='1-1/4 \"':
                OD=1.660
                ID=OD-0.140*2
            elif NomDim=='1-1/2 \"':
                OD=1.900
                ID=OD-0.145*2
            elif NomDim=='2 \"':
                OD=2.375
                ID=OD-0.154*2
            else:
                print "Invalid selection"
                isOK=False
                
        if self.cmbMaterial.GetValue()=="Steel - Schedule 40":
            NomDim=self.cmbNomDim.GetValue()
            if NomDim=='1/4 \"':
                OD=0.540
                ID=OD-0.088*2
            elif NomDim=='3/8 \"':
                OD=0.675
                ID=OD-0.091*2
            elif NomDim=='1/2 \"':
                OD=0.840
                ID=OD-0.109*2
            elif NomDim=='3/4 \"':
                OD=1.050
                ID=OD-0.113*2
            elif NomDim=='1 \"':
                OD=1.315
                ID=OD-0.133*2
            elif NomDim=='1-1/4 \"':
                OD=1.660
                ID=OD-0.140*2
            elif NomDim=='1-1/2 \"':
                OD=1.900
                ID=OD-0.145*2
            elif NomDim=='2 \"':
                OD=2.375
                ID=OD-0.154*2
            else:
                print "Invalid selection"
                isOK=False
                
        if isOK==True:
            self.ODTarget.SetValue('%0.6f' % (OD*0.0254))
            self.IDTarget.SetValue('%0.6f' % (ID*0.0254))
        else:
            dlg = wx.MessageDialog(self,"Invalid selection - try again.  \n Not all dimensions defined for all materials and schedules ")
            dlg.ShowModal()
        
            
            

# end of class TubeSelectClass

