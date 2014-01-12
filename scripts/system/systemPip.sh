#!/bin/sh

# =============================================================================
# Scripts Variables General
# =============================================================================

export pipName=pip
export pipCommandInstall=install
export pipCommandUpgrade=--upgrade

# =============================================================================
# Scripts Variables Local
# =============================================================================

export packageDistribute=distribute
export packageFeedparser=feedparser
export packagePywws=pywws
export packageTweepy=tweepy

# =============================================================================
# Script Functions
# =============================================================================

aptgetFunctionUpgrade() {
	sudo $pipName $pipCommandUpgrade
}

aptgetFunctionInstall() {
	packageName=$@
	sudo $pipName $pipCommandInstall $packageName
}

# =============================================================================
# Script Main
# =============================================================================

aptgetFunctionInstall $packageDistribute
aptgetFunctionInstall $packageFeedparser
aptgetFunctionInstall $packagePywws
aptgetFunctionInstall $packageTweepy

# End of file
