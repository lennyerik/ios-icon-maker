import yaml
import argparse
from os import makedirs
from os.path import exists
from PIL import Image, ImageDraw
from sys import exit

argparser = argparse.ArgumentParser(description='Create diffrent image sizes for iOS Apps')
argparser.add_argument('IMAGE', help='The image to process (has to be 1024x1024px)')
argparser.add_argument('--config', help='Specify a custom config file', default='./config.yaml')
argparser.add_argument('--targets', nargs='+', default=[], help='The targets for the app')
argparser.add_argument('--outdir', default='./out', help='The directory to save the images in')
argparser.add_argument('--preview', action='store_true', help='Also save a preview image')
argparser.add_argument('--previewdir', default='DEFAULT_PREVDIR', help='The directory to save the previews in')
args = argparser.parse_args()

# Remove slashes from paths
if args.outdir[-1:] == '/':
	args.outdir = args.outdir[:-1]

if args.previewdir[-1:] == '/':
	args.previewdir = args.previewdir[:-1]

# Initialise default value for the preview directory
if args.previewdir == 'DEFAULT_PREVDIR':
	args.previewdir = args.outdir + '/preview'

def round_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

print('Reading config...')
with open(args.config, 'r') as configFile:
	config = yaml.safe_load(configFile)

print('')

print('Importing image...')
sourceImage = Image.open(args.IMAGE)
if sourceImage.size != (1024, 1024):
	print('The image has to be 1024x1024px!')
	exit(1)
print('')

if not exists(args.outdir):
	print(args.outdir + ' does not exist. Creating...')
	makedirs(args.outdir)
	print('')


if args.targets != None:
	print('Generating images...')
	print('')

	for target in args.targets:
		
		if target in config['Targets']:
			
			targetfolder = args.outdir + '/' + target
			
			if not exists(targetfolder):
				makedirs(targetfolder)

			print('Generating target: ' + target + '...')

			for resname, res in config['Targets'][target].items():
				filename = target + '_' + resname + '.png'
				print('	- ' + filename)

				if (res, res) != sourceImage.size:
					sourceImage.resize((res, res), Image.BOX).save(targetfolder + '/' + filename)
				else:
					sourceImage.save(targetfolder + '/' + filename)

		
		else:
			print('Target ' + target + ' does not exist in the config.')

		print('')

else:
	print('You should specify targets.')
	print('Otherwise this program does nothing.')


if args.preview:
	if not exists(args.previewdir):
		print('')
		print(args.previewdir + ' does not exist. Creating...')
		makedirs(args.previewdir)

	print('')
	print('Generating previews...')

	for previewName, previewRadius in config['Previews'].items():
		print('	- ' + previewName)
		round_corners(sourceImage, previewRadius).save(args.previewdir + '/' + previewName + '.png')