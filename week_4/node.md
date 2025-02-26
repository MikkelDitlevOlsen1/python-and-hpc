numpy can bothe store row wise and culom wise defult is row wise (order='f' for culm)

numpy have 
shape: shape of aray(2,3)
dtype: type of data in aray
stride how many bytes it need to ove for the next element in eache dimension stride(8,4)

when transposing doesent coppy it changing the shape and stride not the data and therfor transposing dosent help to changhe whtere or not you need to load row wise or culm wise.

views: that a and b point to the same data
np are a littel like pointeres so when you do np.resahape or transform it point to the same data just read it in a difrent form
it can hapen that it make a coppy if it can not strukter based on the ordaenary arary



brodcasting np.arrayes ruelse
brodacasting is when add a+b 
1. line up the shapes to the rhite
2. left-pad the shortest with 1s
3. if an ellement is 1 replace whit larger
4. if all elemetns match: broadcast


profiling
detect where its slow


