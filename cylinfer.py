Python 3.11.14 | packaged by conda-forge | (main, Oct 13 2025, 14:00:26) [MSC v.1944 64 bit (AMD64)] on win32
Type 'help', 'copyright', 'credits' or 'license' for more information.
>>> # Gui.runCommand('Start_Start',0)
>>> # Gui.runCommand('Std_Workbench',7)
>>> # Gui.runCommand('Std_ViewStatusBar',1)
>>> ### Begin command Std_New
>>> App.newDocument()
>>> # App.setActiveDocument("Unnamed")
>>> # App.ActiveDocument=App.getDocument("Unnamed")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed")
>>> # Gui.activeDocument().activeView().viewDefaultOrientation()
>>> ### End command Std_New
>>> # Gui.runCommand('Std_OrthographicCamera',1)
>>> ### Begin command PartDesign_NewSketch
>>> App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
>>> App.getDocument('Unnamed').getObject('Body').AllowCompound = True
>>> # Gui.getDocument('Unnamed').ActiveView.setActiveObject('pdbody',App.getDocument('Unnamed').getObject('Body'),'')
>>> ### End command PartDesign_NewSketch
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',17.4669,16.8133,0)
>>> App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
>>> App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
>>> App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch.')
>>> # import Show
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CreateRectangle',0)
>>> # Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(-18.076498, 11.528136, 0.000000),App.Vector(-18.076498, 26.671381, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-18.076498, 26.671381, 0.000000),App.Vector(-20.076498, 26.671381, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-20.076498, 26.671381, 0.000000),App.Vector(-20.076498, 11.528136, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-20.076498, 11.528136, 0.000000),App.Vector(-18.076498, 11.528136, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
>>> constraintList.append(Sketcher.Constraint('Vertical', 0))
>>> constraintList.append(Sketcher.Constraint('Vertical', 2))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 1))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 3))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,2.000000)) 
>>> constraintList = []
>>> # Gui.runCommand('Sketcher_CreateRectangle',0)
>>> # Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(-76.603104, 27.762791, 0.000000),App.Vector(-76.603104, 17.762791, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-76.603104, 17.762791, 0.000000),App.Vector(-74.603104, 17.762791, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-74.603104, 17.762791, 0.000000),App.Vector(-74.603104, 27.762791, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-74.603104, 27.762791, 0.000000),App.Vector(-76.603104, 27.762791, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 5, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 6, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 6, 2, 7, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 4, 1))
>>> constraintList.append(Sketcher.Constraint('Vertical', 4))
>>> constraintList.append(Sketcher.Constraint('Vertical', 6))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 5))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 7))
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,6,2,2.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,7,2,10.000000)) 
>>> constraintList = []
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch.')
>>> App.getDocument('Unnamed').recompute()
>>> ### Begin command PartDesign_Pad
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
>>> App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
>>> App.getDocument('Unnamed').getObject('Pad').Length = 10
>>> App.ActiveDocument.recompute()
>>> App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pad
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Pad').Length = 5.000000
>>> App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
>>> App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad').SideType = 0
>>> App.getDocument('Unnamed').getObject('Pad').Type = 0
>>> App.getDocument('Unnamed').getObject('Pad').Type2 = 0
>>> App.getDocument('Unnamed').getObject('Pad').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
>>> App.getDocument('Unnamed').getObject('Pad').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad').Offset = 0
>>> App.getDocument('Unnamed').getObject('Pad').Offset2 = 0
>>> App.getDocument('Unnamed').purgeTouched()
>>> App.getDocument('Unnamed').recompute()
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad.Edge4',-18.0765,18.5189,5)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad.Edge3',-18.0765,14.9834,0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad.Edge8',-20.0765,11.5281,3.02089)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad.Edge17',-74.6031,17.7628,2.88769)
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('PartDesign_NewSketch',0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',17.8928,20.1374,0)
>>> App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
>>> App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
>>> App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch001.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch001.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-124.492760, 29.542391, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,3.000000)) 
>>> constraintList = []
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-161.970474, 43.542679, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,3.000000)) 
>>> constraintList = []
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-109.846298, 26.526943, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',2,3.000000)) 
>>> constraintList = []
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch001.')
>>> App.getDocument('Unnamed').recompute()
>>> ### Begin command PartDesign_Pad
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
>>> App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
>>> App.getDocument('Unnamed').getObject('Pad001').Length = 10
>>> App.ActiveDocument.recompute()
>>> App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Pad001').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad001').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Pad001').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad001').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Pad001').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad001').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Pad001').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad001').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Pad001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad001').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad001.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pad
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Pad001').Length = 8.000000
>>> App.getDocument('Unnamed').getObject('Pad001').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad001').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad001').Direction = (0, 0, 1)
>>> App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad001').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad001').SideType = 0
>>> App.getDocument('Unnamed').getObject('Pad001').Type = 0
>>> App.getDocument('Unnamed').getObject('Pad001').Type2 = 0
>>> App.getDocument('Unnamed').getObject('Pad001').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad001').UpToFace2 = None
>>> App.getDocument('Unnamed').getObject('Pad001').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad001').Offset = 0
>>> App.getDocument('Unnamed').getObject('Pad001').Offset2 = 0
>>> App.getDocument('Unnamed').purgeTouched()
>>> App.getDocument('Unnamed').recompute()
>>> App.getDocument('Unnamed').getObject('Pad').Visibility = False
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Face3',-20.0765,16.1834,3.64942)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Face7',-76.6031,19.6217,1.73424)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Face19',-111.04,25.6348,3.0317)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Edge27',-125.616,28.5477,8)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Face16',-162.825,42.3102,4.63265)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Edge30',-163.093,42.548,8)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.Face7',-76.6031,20.394,2.75316)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad001.',-76.6031,20.394,2.75316)
>>> # Gui.runCommand('PartDesign_NewSketch',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',16.7418,12.0846,0)
>>> App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
>>> App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
>>> App.getDocument('Unnamed').getObject('Sketch002').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch002.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch002.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> # Gui.runCommand('Sketcher_CreateRectangle',0)
>>> # Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch002.')
>>> App.getDocument('Unnamed').recompute()
>>> ### Begin command PartDesign_Pad
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad002')
>>> App.getDocument('Unnamed').getObject('Pad002').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
>>> App.getDocument('Unnamed').getObject('Pad002').Length = 10
>>> App.ActiveDocument.recompute()
>>> App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'),['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad002').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad002').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad002').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad002').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad002').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad002.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pad
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Pad002').Length = 3.000000
>>> App.getDocument('Unnamed').getObject('Pad002').Length2 = 10.000000
>>> App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad002').TaperAngle2 = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Direction = (1, 1, 1)
>>> App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad002').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad002').SideType = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Type = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Type2 = 0
>>> App.getDocument('Unnamed').getObject('Pad002').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad002').UpToFace2 = None
>>> App.getDocument('Unnamed').getObject('Pad002').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Offset = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Offset2 = 0
>>> App.getDocument('Unnamed').purgeTouched()
>>> App.getDocument('Unnamed').getObject('Pad002').Length = 3.000000
>>> App.getDocument('Unnamed').getObject('Pad002').Length2 = 10.000000
>>> App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad002').TaperAngle2 = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Direction = (1, 1, 1)
>>> App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad002').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad002').SideType = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Type = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Type2 = 0
>>> App.getDocument('Unnamed').getObject('Pad002').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad002').UpToFace2 = None
>>> App.getDocument('Unnamed').getObject('Pad002').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Offset = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Offset2 = 0
>>> App.getDocument('Unnamed').purgeTouched()
>>> App.getDocument('Unnamed').recompute()
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> # Gui.runCommand('PartDesign_NewSketch',0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',13.7172,15.8992,1.9166e-14)
>>> App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch003')
>>> App.getDocument('Unnamed').getObject('Sketch003').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
>>> App.getDocument('Unnamed').getObject('Sketch003').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch003.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch003')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch003.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch003')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CreateRectangle',0)
>>> # Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch003')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(-84.630577, 3.257422, 0.000000),App.Vector(-84.630577, -76.742578, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-84.630577, -76.742578, 0.000000),App.Vector(-4.630577, -76.742578, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-4.630577, -76.742578, 0.000000),App.Vector(-4.630577, 3.257422, 0.000000)))
>>> geoList.append(Part.LineSegment(App.Vector(-4.630577, 3.257422, 0.000000),App.Vector(-84.630577, 3.257422, 0.000000)))
>>> App.getDocument('Unnamed').getObject('Sketch003').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
>>> constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
>>> constraintList.append(Sketcher.Constraint('Vertical', 0))
>>> constraintList.append(Sketcher.Constraint('Vertical', 2))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 1))
>>> constraintList.append(Sketcher.Constraint('Horizontal', 3))
>>> App.getDocument('Unnamed').getObject('Sketch003').addConstraint(constraintList)
>>> del constraintList
>>> 
>>> App.getDocument('Unnamed').getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,80.000000)) 
>>> App.getDocument('Unnamed').getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,80.000000)) 
>>> constraintList = []
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch003')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch003.')
>>> App.getDocument('Unnamed').recompute()
>>> ### Begin command PartDesign_Pad
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad002')
>>> App.getDocument('Unnamed').getObject('Pad002').Profile = (App.getDocument('Unnamed').getObject('Sketch003'), ['',])
>>> App.getDocument('Unnamed').getObject('Pad002').Length = 10
>>> App.ActiveDocument.recompute()
>>> App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch003'),['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Sketch003').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad002').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad002').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad002').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad002').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Pad002').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad002').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad002.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pad
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Pad002').Length = 3.000000
>>> App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Direction = (0, 0, 1)
>>> App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch003'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad002').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad002').SideType = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Type = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Type2 = 0
>>> App.getDocument('Unnamed').getObject('Pad002').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad002').UpToFace2 = None
>>> App.getDocument('Unnamed').getObject('Pad002').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Offset = 0
>>> App.getDocument('Unnamed').getObject('Pad002').Offset2 = 0
>>> App.getDocument('Unnamed').purgeTouched()
>>> App.getDocument('Unnamed').recompute()
>>> App.getDocument('Unnamed').getObject('Pad001').Visibility = False
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.getDocument('Unnamed').getObject('Sketch003').Visibility = False
>>> # Gui.runCommand('PartDesign_NewSketch',0)
>>> # Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',18.7225,17.0436,0)
>>> App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch004')
>>> App.getDocument('Unnamed').getObject('Sketch004').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
>>> App.getDocument('Unnamed').getObject('Sketch004').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch004.')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch004.'))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> import PartDesignGui
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> # Gui.Selection.clearSelection()
>>> # Gui.runCommand('Sketcher_CreateCircle',0)
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-184.163406, 42.639057, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch004').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch004').addConstraint(Sketcher.Constraint('Diameter',0,3.000000)) 
>>> constraintList = []
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-168.248932, 52.619324, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch004').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch004').addConstraint(Sketcher.Constraint('Diameter',1,3.000000)) 
>>> constraintList = []
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-145.860764, 48.843006, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch004').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch004').addConstraint(Sketcher.Constraint('Diameter',2,3.000000)) 
>>> constraintList = []
>>> # Gui.runCommand('Sketcher_CompCreateConic',0)
>>> ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> 
>>> lastGeoId = len(ActiveSketch.Geometry)
>>> 
>>> geoList = []
>>> geoList.append(Part.Circle(App.Vector(-123.472603, 48.843006, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.500000))
>>> App.getDocument('Unnamed').getObject('Sketch004').addGeometry(geoList,False)
>>> del geoList
>>> 
>>> constraintList = []
>>> App.getDocument('Unnamed').getObject('Sketch004').addConstraint(Sketcher.Constraint('Diameter',3,3.000000)) 
>>> constraintList = []
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.ActiveDocument.recompute()
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch004')
>>> # tv = ActiveSketch.ViewObject.TempoVis
>>> # if tv:
>>> #   tv.restore()
>>> # ActiveSketch.ViewObject.TempoVis = None
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # Gui.Selection.addSelection('Unnamed','Body','Sketch004.')
>>> App.getDocument('Unnamed').recompute()
>>> ### Begin command PartDesign_Pad
>>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad003')
>>> App.getDocument('Unnamed').getObject('Pad003').Profile = (App.getDocument('Unnamed').getObject('Sketch004'), ['',])
>>> App.getDocument('Unnamed').getObject('Pad003').Length = 10
>>> App.ActiveDocument.recompute()
>>> App.getDocument('Unnamed').getObject('Pad003').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch004'),['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Sketch004').Visibility = False
>>> App.ActiveDocument.recompute()
>>> # App.getDocument('Unnamed').getObject('Pad003').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad002').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad003').ViewObject.ShapeAppearance)
>>> # App.getDocument('Unnamed').getObject('Pad003').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad002').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad003').ViewObject.LineColor)
>>> # App.getDocument('Unnamed').getObject('Pad003').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad002').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad003').ViewObject.PointColor)
>>> # App.getDocument('Unnamed').getObject('Pad003').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad002').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad003').ViewObject.Transparency)
>>> # App.getDocument('Unnamed').getObject('Pad003').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad002').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad003').ViewObject.DisplayMode)
>>> # Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad003.')
>>> # Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pad
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('Unnamed').getObject('Pad003').Length = 8.000000
>>> App.getDocument('Unnamed').getObject('Pad003').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad003').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad003').Direction = (0, 0, 1)
>>> App.getDocument('Unnamed').getObject('Pad003').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch004'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad003').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad003').SideType = 0
>>> App.getDocument('Unnamed').getObject('Pad003').Type = 0
>>> App.getDocument('Unnamed').getObject('Pad003').Type2 = 0
>>> App.getDocument('Unnamed').getObject('Pad003').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad003').UpToFace2 = None
>>> App.getDocument('Unnamed').getObject('Pad003').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad003').Offset = 0
>>> App.getDocument('Unnamed').getObject('Pad003').Offset2 = 0
>>> App.getDocument('Unnamed').purgeTouched()
>>> App.getDocument('Unnamed').recompute()
>>> App.getDocument('Unnamed').getObject('Pad002').Visibility = False
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.getDocument('Unnamed').getObject('Sketch004').Visibility = False
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.Face27',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.Face27',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.Face27',-51.2837,-17.9995,3)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.Edge27',-125.616,28.5477,8)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.',-125.616,28.5477,8)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','',-125.616,28.5477,8)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Body','Pad003.Edge27',-125.616,28.5477,8)
>>> ### Begin command Std_SendToPythonConsole
>>> # try:
>>> #     del(doc,lnk,obj,shp,sub,subs)
>>> # except Exception:
>>> #     pass
>>> # 
>>> # doc = App.getDocument("Unnamed")
>>> # obj = doc.getObject("Pad003")
>>> # shp = obj.Shape
>>> # sub = obj.getSubObject("Edge27")
>>> ### End command Std_SendToPythonConsole
>>> 