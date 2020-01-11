import xbmc, xbmcaddon
import simplejson as json

#don't use this, as the instance does not get updated --> no setting update
#https://forum.kodi.tv/showthread.php?tid=290353&pid=2425543#pid2425543
#ADDON = xbmcaddon.Addon()
ADDONNAME = xbmcaddon.Addon().getAddonInfo('id')

def log(message, level=xbmc.LOGNOTICE):
    xbmc.log('[%s] %s' % (ADDONNAME, message), level)

def getSetting(opt):
    return xbmcaddon.Addon().getSetting(opt)

def getAddonVersion():
    return xbmcaddon.Addon().getAddonInfo('version')

def getAddonChangelog():
    return xbmcaddon.Addon().getAddonInfo('changelog')

def getBoolSetting(opt):
    """ With Kodi 18 native api available """
    return True if xbmcaddon.Addon().getSetting(opt).upper() == "TRUE" else False

def setSetting(opt, value):
    return xbmcaddon.Addon().setSetting(opt, value)

def openSettings():
    xbmcaddon.Addon().openSettings()

def getLS(nr):
    return xbmcaddon.Addon().getLocalizedString(nr)

def validateAuthToken(authToken):
    return True if len(authToken) == 36 else False

def updateSavedAddonVersion():
    setSetting('currAddonVersion', getAddonVersion())
    
def intToCompString(comp):
    switch = {
        0: "GRABBER",
        1: "V4L",
        2: "LEDDEVICE",
        3: "SMOOTHING",
        4: "BLACKBORDER",
        5: "FORWARDER",
        6: "UDPLISTENER",
        7: "BOBLIGHTSERVER",
        8: "ALL",
    }
    return switch.get(comp, "NOT_FOUND")

def modeTo3D(mode=None):
    switch = {
        "split_vertical": "3DSBS",
        "split_horizontal": "3DTAB",
    }
    return switch.get(mode, "2D")

def getStereoscopeMode():
    try:
        response = json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"GUI.GetProperties","params":{"properties":["stereoscopicmode"]},"id":669}'))
        mode = response["result"]["stereoscopicmode"]["mode"]
        return modeTo3D(mode)

    except:
        log("getStereoscopeMode() has thrown an exception!")
        return modeTo3D()
