import sys, glob
from PIL import Image
deck=sys.argv[1]; cols=int(sys.argv[2]) if len(sys.argv)>2 else 3
fs=sorted(glob.glob(f"/home/claude/corum/shots/{deck}/[0-9]*.jpg"))
start=int(sys.argv[3]) if len(sys.argv)>3 else 0; cnt=int(sys.argv[4]) if len(sys.argv)>4 else 9
fs=fs[start:start+cnt]
ims=[Image.open(f).resize((960,540)) for f in fs]
rows=(len(ims)+cols-1)//cols
c=Image.new("RGB",(960*cols,540*rows),"white")
for i,im in enumerate(ims): c.paste(im,((i%cols)*960,(i//cols)*540))
c.save(f"/home/claude/corum/shots/{deck}_sheet_{start}.jpg", quality=80); print(fs[0], fs[-1])
