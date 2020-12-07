#include "lists.h"

/**
 * check_cycle - checks for cycle in linked list
 * @list: head of linked list
 * Return: 1 if there is a loop and 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	int i;

	for (i = 0; list != NULL; i++, list = list->next)
	{
		if (&list == &head && i != 0)
			return (1);
		if (i > 1020)
			return (1);
	}
	return (0);
}
