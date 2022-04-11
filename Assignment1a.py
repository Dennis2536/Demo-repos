# the input accepts month=['Jan', 'Feb',  'Mar', 'Apr' , 'May', 'Jun' ,  'Jul', 'Aug', 'Sep' , 'Oct', 'Nov' , 'Dec']
# the first line is user input
month=input('Enter a month:')

# assign S to the  months with 31 days 
S = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']

# assign T to the months with 30 days
T = ['Apr', 'Jun', 'Sep', 'Nov']

# the first if statement

if month in S:
#  these lines are indented with tab
    print('There are 31 days in %s' %month)
    if month=='Mar':
        print('March is the current month!')
else:
    if month in T:
        print('There are 30 days in %s' %month)
    elif month=='Feb':
        print('There are 28 days in %s' %month)
    

