start /b /wait python -c "import time; time.sleep(5); print 'first'"
echo done1
start /b /wait python -c "import time; print 'second'"
echo done2
