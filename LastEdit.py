import sublime, sublime_plugin

class LastEditCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        lastView,lastViewLine = getLastEditLine()
        
        # sel = self.view.sel()[0]
        # curr_line,_ = self.view.rowcol(sel.begin())

        # if curr_line == lastViewLine and self.view.id() == lastView:
        #     lastView,lastViewLine = getLastEditLine()

        lastViewCol = RecordIntputRegion.editLine[lastView][lastViewLine]
        jumpLastPoint(jumpLastView(lastView),lastViewLine,lastViewCol)
class SwitchEditViewCommand(sublime_plugin.TextCommand):
    def run(self, edit,way="left"):
        if way == "left":
            lastView = RecordIntputRegion.editView.pop();
            RecordIntputRegion.editView.insert(0,lastView);
            if lastView == self.view.id():
                lastView = RecordIntputRegion.editView.pop();
                RecordIntputRegion.editView.insert(0,lastView);
        else:
            lastView = RecordIntputRegion.editView.pop(0);
            RecordIntputRegion.editView.append(lastView);
            if lastView == self.view.id():
                lastView = RecordIntputRegion.editView.pop(0);
                RecordIntputRegion.editView.append(lastView);
        jumpLastView(lastView)

def jumpLastView(lastView):
    lastViewObj=None
    for window in sublime.windows():
        for view in window.views():
            if lastView == view.id():
                lastViewObj = view
                lastWindow  = window
                pass
    lastGroup,_ = lastWindow.get_view_index(lastViewObj)
    lastWindow.focus_group(lastGroup) 

    lastWindow.focus_view(lastViewObj)

    return lastViewObj

def jumpLastPoint(lastViewObj,lastViewLine,lastViewCol):
    pt = lastViewObj.text_point(lastViewLine,lastViewCol);
    lastViewObj.sel().clear();

    lastViewObj.sel().add(sublime.Region(pt));

    lastViewObj.show(pt);

def getLastEditLine():
    viewsCount = len(RecordIntputRegion.lastView)-1;
    lastView = RecordIntputRegion.lastView[viewsCount];
    lastViewPosKey = str(lastView)+":"+str(viewsCount);
    if len(RecordIntputRegion.lastLine[lastViewPosKey]) == 0:
        RecordIntputRegion.lastView.pop();
        viewsCount = len(RecordIntputRegion.lastView)-1;
        lastView = RecordIntputRegion.lastView[viewsCount];
        lastViewPosKey = str(lastView)+":"+str(viewsCount);
    lastViewLine = RecordIntputRegion.lastLine[lastViewPosKey].pop()
    return lastView,lastViewLine

class RecordIntputRegion(sublime_plugin.EventListener):
    editLine =   {}
    lastLine =   {}
    lastView = []
    editView = []

    def on_modified(self, view):
        sel = view.sel()[0]

        curr_view = view.id()
        curr_window = view.window().id()
        last_line,last_col = view.rowcol(sel.begin())
        lastViewPos = len(RecordIntputRegion.lastView)-1
        lastSwitchViewPos = len(RecordIntputRegion.editView)-1

        if lastViewPos == -1:
            RecordIntputRegion.lastView.append(curr_view)
            lastViewPos += 1
            pass

        if not RecordIntputRegion.lastView[lastViewPos] is curr_view:
            RecordIntputRegion.lastView.append(curr_view)
            lastViewPos += 1
        if lastSwitchViewPos == -1:
            RecordIntputRegion.editView.append(curr_view)
            lastSwitchViewPos += 1
            pass

        if not RecordIntputRegion.editView[lastSwitchViewPos] is curr_view:
            RecordIntputRegion.editView.append(curr_view)


        viewPosKey = str(curr_view)+":"+str(lastViewPos)
        if not RecordIntputRegion.lastLine.has_key(viewPosKey):
            RecordIntputRegion.lastLine[viewPosKey]=[]
            pass

        lastLinePos = len(RecordIntputRegion.lastLine[viewPosKey]) -1;
        

        if lastLinePos == -1:
            RecordIntputRegion.lastLine[viewPosKey].append(last_line);
            lastLinePos +=1;

        if not RecordIntputRegion.lastLine[viewPosKey][lastLinePos] is last_line:
            RecordIntputRegion.lastLine[viewPosKey].append(last_line)
            pass

        if not RecordIntputRegion.editLine.has_key(curr_view):
            RecordIntputRegion.editLine[curr_view]={}
            pass
        RecordIntputRegion.editLine[curr_view][last_line] = last_col

