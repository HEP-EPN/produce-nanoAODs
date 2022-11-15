
# this file attempts to split a text file containing filepaths into separate text files with groups of 10
# ideally the outputs are then used as inputs to the miniAOD production script

# takes file as argument (example: /home/hep/ekauffma/analysis-grand-challenge/datasets/cms-open-data-2015/ttbar/19978.txt)

import sys
import argparse

def main(filepath, nfiles, outpath):
	
	splitpath = filepath.replace('.', '/').split('/')
	prefix = "cmsopendata2015" + "_" + splitpath[-3] + "_" + splitpath[-2]
	
	openfile = open(filepath,"r")
	openfilelines = openfile.readlines()
	
	splitline = openfilelines[0].split('/')
	splitline = [string for string in splitline if string != '']
	dirnumber_prev = splitline[-2]
	filetype_prev = splitline[-3]
	dirnumber = splitline[-2]
	filetype = splitline[-3]
	
	filelist = []
	
	i = 0
	filecount = 0
	while i<len(openfilelines):
		while dirnumber==dirnumber_prev and filetype==filetype_prev and len(filelist)<nfiles and i<len(openfilelines):
	
			rootfile = openfilelines[i]
			splitline = rootfile.split('/')
			splitline = [string for string in splitline if string != '']
		
	
			dirnumber = splitline[-2]
			filetype = splitline[-3]
	
			filelist.append(rootfile)
			i+=1
			
		suffix = f'_{filetype_prev}_{dirnumber_prev}_{filecount:04d}.txt'
		newfilepath = outpath + prefix + suffix
	
		with open(newfilepath, 'w') as f:
			f.writelines(filelist)
	
		print(f'file {newfilepath} created')
	
		if len(filelist)==nfiles:
			filecount+=1
		else:
			filecount = 0
	
		dirnumber_prev = splitline[-2]
		filetype_prev = splitline[-3]
		filelist=[]	
	
	openfile.close()

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='This program takes in a text file containing a list of ROOT files and produces multiple text files, listing the ROOT files in groups of nfiles.')
	parser.add_argument("filepath", help="Path to input text file containing list of ROOT files", type=str)
	parser.add_argument("-n","--nfiles",help="Number of files to group together (decide by considering the desired size of the output file)", default=10, type=int)
	parser.add_argument("-o","--outpath",help="Path to write output text files to",default="",type=str)


	args = parser.parse_args()
	
	main(args.filepath, args.nfiles, args.outpath)
