# Icon Maker
A CLI-Tool for creating appropriate icon sizes for iPhone, iPad, Apple Watch and the App Store

## Installation
Make sure you have python3 and pip installed:

    sudo apt-get install -y python3
    sudo apt-get install -y python3-pip

Or for non-debian distributions with pacman as default:

    pacman -S python3
    pacman -S python3-pip

Now clone the repo and install the required libraries

    git clone https://github.com/lennyerik/ios-icon-maker.git
    cd ios-icon-maker
    pip3 install -r requirements.txt

## Usage

    python3 IconMaker.py [ARGUMENTS] [IMAGE]

IMAGE is a 1024x1024px image of your icon.

To show a list of avaliable arguments, run:

    python3 IconMaker.py -h

### Example Usage
### Creating an Icon for iPhone and the App Store

    python3 IconMaker.py MyIcon.png --targets iPhone App_Store

### Creating an Icon for iPhone, Apple Watch and Previews

    python3 IconMaker.py --targets iPhone Apple_Watch --preview

## Configuration
### Advanced configuration options
For advanced configuration options you can either edit the config.yaml file in the script's directory or create your own [yaml](https://en.wikipedia.org/wiki/YAML) configuration file.

### The config.yaml file
#### Targets
Targets consist of different images.  
The iPhone target, for example, has icons for notifications, the home screen, settings...  
In the yaml file the icons consist of a name and the size:
`Notification_2x: 40`  
This would be an icon named Notification_2x with a size of 40x40px.  

**Every icon is later automatically prefixed with the target's name and an underscore.**

#### Previews
To create new preview views, add them in in the config.yaml.  

``iPhone: 130``  
This, for example is the preview for iPhone icons.  
Every preview has a name, which in this case is iPhone and a corner-radius for the rounding of the corners, which, in this example is 130px.

### Moaaaaaarrrrrrr configuration!!!
If you need more control over the creation of your icons feel free to look into and modify the [python](https://www.python.org/) code.
