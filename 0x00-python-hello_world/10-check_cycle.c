#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Checks if a single linked list has a cycle.
 *
 * @list: Pointer to the begining of a single linked list.
 *
 * Description - This program takes a single linked list and determines
 *               if said list contains a cycle within it.
 *
 * Return: → 1 if the list has a cycle.
 *         → 0 if the list has no cycle.
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *wabit, *tultre;

	if (list == NULL)
		return (0);

	wabit = list;
	tultre = list;

	while (wabit != NULL && tultre != NULL)
	{
		wabit = wabit->next->next;
		tultre = tultre->next;
		if (wabit == tultre)
			return (1);
	}
	return (0);
}
