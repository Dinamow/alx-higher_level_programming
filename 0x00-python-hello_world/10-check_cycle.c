#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp, *reset;
	temp = list;
	reset = list;
	list = list->next;
	while(list)
	{
		list = list->next;
		if (list == temp)
			return (1);
		temp = temp->next;
	}
	list = reset;
	return (0);
}
