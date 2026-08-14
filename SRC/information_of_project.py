'''

#-----------user_service.py-------------

      To run user_service.py 
      create first this table in mysql:
      Query:

      Its store the all user its register

      CREATE TABLE member (
         email VARCHAR(100),
         login_pass varchar(100),
         num varchar(10),
         roll varchar(8)
     );

     Its store the information of only student 

     CREATE TABLE student (
         email VARCHAR(100),
         login_pass varchar(100),
         num varchar(10),
         roll varchar(8)
     );

     Its store the inforemation about inly teacher

     CREATE TABLE teacher (
         email VARCHAR(100),
         login_pass varchar(100),
         num varchar(10),
         roll varchar(8)
     );
     
'''
'''

#------------document_servise.py------------

    return the file path the function name is 
    open_file_workflow 
    only run this file and catch the file_path in variable 

    Also file path store in tha database table 
    Query:
    CREATE TABLE file_path (
		  file_path VARCHAR(500)
    );

'''