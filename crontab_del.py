
# sudo apt-get install python-crontab

from crontab import CronTab
import youless

def main():
    cron = CronTab(user= True)
    #job = cron.find_command("python youless.py")
    cron.remove_all()
    cron.write()
    print("Die Messung wurde gestoppt")



if __name__ == "__main__":
    main()





