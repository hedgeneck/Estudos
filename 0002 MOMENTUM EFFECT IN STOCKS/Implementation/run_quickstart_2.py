{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Esta é uma simples implementação do código encontrado em\n",
    "# https://www.backtrader.com/docu/quickstart/quickstart/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting Portfolio Value: 100000.00\n",
      "Final Portfolio Value: 100000.00\n"
     ]
    }
   ],
   "source": [
    "from __future__ import (absolute_import, division, print_function,\n",
    "                        unicode_literals)\n",
    "\n",
    "import datetime  # For datetime objects\n",
    "import os.path  # To manage paths\n",
    "import sys  # To find out the script name (in argv[0])\n",
    "\n",
    "# Import the backtrader platform\n",
    "import backtrader as bt\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # Create a cerebro entity\n",
    "    cerebro = bt.Cerebro()\n",
    "\n",
    "    # Datas are in a subfolder of the samples. Need to find where the script is\n",
    "    # because it could have been called from anywhere\n",
    "    # os.path.basename() pega o último elemento\n",
    "    # \"path/to/project/foo.py\".split(\"/\")[-1] retorna \"foo.py\"\n",
    "    # http://www.devfuria.com.br/python/os-path/\n",
    "    # modpath = os.path.dirname(os.path.abspath(sys.argv[0]))\n",
    "    # o join junta as duas partes com um //\n",
    "    # datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')\n",
    "\n",
    "    datapath = 'oracle.txt'\n",
    "    \n",
    "    # Create a Data Feed\n",
    "    data = bt.feeds.YahooFinanceCSVData(\n",
    "        dataname=datapath,\n",
    "        # Do not pass values before this date\n",
    "        fromdate=datetime.datetime(2000, 1, 1),\n",
    "        # Do not pass values after this date\n",
    "        todate=datetime.datetime(2000, 12, 31),\n",
    "        reverse=False)\n",
    "\n",
    "    # Add the Data Feed to Cerebro\n",
    "    cerebro.adddata(data)\n",
    "\n",
    "    # Set our desired cash start\n",
    "    cerebro.broker.setcash(100000.0)\n",
    "\n",
    "    # Print out the starting conditions\n",
    "    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())\n",
    "\n",
    "    # Run over everything\n",
    "    cerebro.run()\n",
    "\n",
    "    # Print out the final result\n",
    "    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
