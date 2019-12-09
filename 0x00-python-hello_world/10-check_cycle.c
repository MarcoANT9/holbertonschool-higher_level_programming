#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Checks if a single linked list has a cycle.
 *
 * @list: Pointer to the begining of a single linked list.
 *
 *
 *
 * Description - This program takes a single linked list and determines
 *               if said list contains a cycle within it.
 *
 *
 *
 * Return: → 1 if the list has a cycle.
 *         → 0 if the list has no cycle.
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *checker;

	checker = list->next;

	while (checker != NULL)
	{
		if (checker == list)
			return (1);
		checker = checker->next;
	}

	return (0);

}
