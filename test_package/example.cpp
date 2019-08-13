#include <iostream>
#include <libbar/libbar.h>

int main() {
	libbar::run_me();

	if (libbar::question_of_life() != 42)
	{
		std::cout << "The answer to the question of life and everything should be 42, was " << libbar::question_of_life() << std::endl;
		return 1;
	}

	return 0;
}
