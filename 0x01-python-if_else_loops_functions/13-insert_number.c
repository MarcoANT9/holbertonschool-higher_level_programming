#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a new node in an organized linked list
 *
 * @head: Head of the linked list.
 * @number: Data to insert in the linked list.
 *
 *
 * Description - This function takes an organized linked list and a data value
 *               and creates a new node with the value respecting the order in
 *               the list.
 *
 *
 * Return: → Address of the new node on success.
 *         → NULL on failure.
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	int index = 0;
	listint_t *current_node, *tmp_address;
	listint_t *added_node = malloc(sizeof(listint_t));

	if (added_node == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = added_node;
		added_node->n = number;
		added_node->next = NULL;
		return (added_node);
	}
	added_node->n = number;
	current_node = *head;
	tmp_address = *head;
	while (tmp_address->n < number && tmp_address->next != NULL)
	{
		if (index != 0)
			current_node = current_node->next;
		index++;
		tmp_address = tmp_address->next;
	}
	if (tmp_address->next == NULL)
		added_node->next = NULL;
	else
		added_node->next = tmp_address;
	current_node->next = added_node;
	return (added_node);
}
