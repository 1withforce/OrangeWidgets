from sys import argv
import itertools

script, usr_file = argv

#function that simply identifies a line as a header or not

def find_header(head):
    return head[0] == '>'

with open('usr_file') as fa:
 	print len(list(itertools.groupby(fa, key=find_header)))//2

# the groups will simply alternate between a group of header lines, 
# and a group of non-header lines

def fasta_reader(file):
  for header,group in itertools.groupby(fa, find_header):
    if header:
      head = group.next()
      header_id = head[1:].split()[0]
    else:
      sequence = ''.join(head.strip() for head in group)
      yield header_id, sequence

with open('usr_file') as fa:
  d = dict(fasta_reader(fa))
