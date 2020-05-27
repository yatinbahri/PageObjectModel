

def desired_capabilities(self):
    '''
    Real device
    '''
    return dict (platformName= 'Android',
            deviceName= '8UEDU18714000545',
            remote_url= 'http://localhost:4723/wd/hub',
            platform_version='8.0.0',
            appActivity= 'com.digix.althrmy.staging.MainActivity',
            appPackage= 'com.digix.althrmy.staging',
            automationName= 'uiautomator2',
            useJSONSource= True,
            autoGrantPermissions=  True,
            simpleIsVisibleCheck= True)
