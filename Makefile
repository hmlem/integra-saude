init:
	flask cli initial-seed
	flask cli create-user "Filipe Lopes" contato@filipelopes.me root
	flask cli create-user-test