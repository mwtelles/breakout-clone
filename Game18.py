import cfg
from modules.game import breakoutClone


def main():
	game = breakoutClone(cfg)
	game.run()

if __name__ == '__main__':
	main()