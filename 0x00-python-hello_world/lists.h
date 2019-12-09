#ifndef LISTS_H
#define LISTS_H

/**========================================================================*/
/**-LIBRARIES--------------------------------------------------------------*/
/**========================================================================*/

#include <stdlib.h>


/**========================================================================*/
/**-STRUCTURES-& DEFINITIONS-----------------------------------------------*/
/**========================================================================*/

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;


/**========================================================================*/
/**-FUNCTIONS--------------------------------------------------------------*/
/**========================================================================*/

/** Defined by default */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
/**====================*/

/** Checks if a single linked list has a cycle */
int check_cycle(listint_t *list);







#endif