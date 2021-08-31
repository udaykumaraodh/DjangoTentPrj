# DjangoTentPrj
Work on DjangoTenant project

--download the project and open it visual code or pycharm

--open the mytestenv to activate the virtual environment
cd F:\Rtp Project\office\DemoPrj_tent\mytestenv\Scripts\activate

--after entering into the virtual enviroment install the required packages from the 
requirements.txt attached in the project

--pip install requirements.txt

create tables and schemas in your pgadmin2
 by
--python manage.py makemigrations
--python manage.py migrate


already  sharedapps and tenantapps are set according to requierment

-- To create a new tenant
---------------------------

---python manage.py create_tenant
  enter schema :xyz
  enter name:xyz
  enter host:xyz.localhost:8000

To run tenat user:

In browser enter xyz.localhost:8000/admin
                                   /urls
 


