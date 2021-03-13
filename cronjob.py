

#!/usr/bin/crontab

from crontab import CronTab
import youless
import data_summary

def main():
    cron = CronTab(user= True)
    job0 = cron.new(command="python data_summary.py")
    job1 = cron.new(command="sleep 5; python youless.py")
    job2 = cron.new(command="sleep 15; python youless.py")
    job3 = cron.new(command="sleep 25; python youless.py")
    job4 = cron.new(command="sleep 35; python youless.py")
    job5 = cron.new(command="sleep 45; python youless.py")
    job6 = cron.new(command="sleep 55; python youless.py")

    job0.minute.every(1)
    job1.minute.every(1)
    job2.minute.every(1)
    job3.minute.every(1)
    job4.minute.every(1)
    job5.minute.every(1)
    job6.minute.every(1)

    job0.enable()
    job1.enable()
    job2.enable()
    job3.enable()
    job4.enable()
    job5.enable()
    job6.enable()

    cron.write()
    print("Die Messung wurde gestartet")


if __name__ == "__main__":
    main()


