def build_pyramid(height : int) -> str:
    # to-do
    string_piramid = ""
    piramyd = ["#","##","###","####","#####","######","#######","########","#########"]
    
    for i in range(height):
        j=0
        while j < height:
            print("Oi")
            string_piramid += "\s"
            j+=1
            if j == height:
                string_piramid += "\n" +piramyd[i]
        
    print(string_piramid)
    
    
build_pyramid(3)
