Домашнее задание #8
-------------------

Задание 1.
==========
Исследуем файловую систему ``/proc``.
+++++++++++++++++++++++++++++++++++++

В Linux и других операционных системах \*nix специальная файловая система ``procfs`` позволяет получить мгновенный снимок состояния системы. Эта файловая система монтируется в ``/proc`` и обычно называется виртуальной, потому что представленные в ней файлы являются фактически интерфейсами, позволяющими получать или задавать информацию о работе системы. Например, команда::

    > cat /proc/cpuinfo

выведет информацию о центральном процессоре, но размер самого файла ``/proc/cpuinfo`` нулевой. Нас будут интересовать директории вида ``/proc/<PID>``, которые соответствуют процессам. Например, ``/proc/1674`` содержит информацию о процессе с ID 1674. Некоторые файлы, содержащиеся в директориях ``/proc/<PID>``:

    1. ``/proc/<PID>/cmdline`` - командная строка, которой был запущен процесс.
    2. ``/proc/<PID>/cwd`` - символическая ссылка на текущую рабочую директорию процесса.
    3. ``/proc/<PID>/environ`` - список переменных окружения для процесса.
    4. ``/proc/<PID>/smaps`` - маппинги памяти. Пока для простоты можно считать, что этот файл позволяет как процесс использует память.

В последнем из перечисленных файлов, в частности, для каждого маппинга указан объем используемого swap-пространства, т.е. объем данных выгруженных из памяти на диск. Своппинг часто снижает производительность процесса, поскольку доступ к диску происходит гораздо медленнее, чем доступ к оперативной памяти.

Существует несколько способов узнать, сколько же свопа использует процесс, но мы сделаем это напрямую - используя файл ``/proc/<PID>/smaps``. Это сделано в скрипте ``process-swap.sh``. После запуска::

    > sh process-swap.sh <PID>

он выводит информацию в виде::

    Total swap space used by process <PID> (<CMDLINE>): <TOTALSWAP> kB

Логика работы описана в комментариях. Попробуйте запустить это скрипт для процесса с реальным ID. Для некоторых процессов придется использовать ``sudo``.

Ссылки
++++++

1. `bash Cookbook`, Carl Albing, JP Vossen, Cameron Newham, O'Reilly, 2007.