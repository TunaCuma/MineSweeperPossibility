# MineSweeperPossibility
Tool for calculating the possibility of one click win in the minesweeper game for different grid sizes and mine amounts

For calculating the possibility of situations such as these:
![image](https://user-images.githubusercontent.com/62616668/213732870-82c4baf8-897c-4df6-8166-567545713378.png)
https://minesweepergame.com/website/authoritative-minesweeper/wiki/File:OneClickBug-DamienMoore-260301.jpg
![image](https://user-images.githubusercontent.com/62616668/213733142-0427e4e3-8ee5-4864-bee8-a152127f7f54.png)
https://minesweepergame.com/website/authoritative-minesweeper/wiki/File:OneClickBug-TimKostka-2002.gif

This code initilazes every possible mine placement on a grid and then evaluates every one of them to count how many mine placements are there for perfect game.

Sadly, big O for this code is too high so it takes too long to calculate  bigger grids. Im open for any help
